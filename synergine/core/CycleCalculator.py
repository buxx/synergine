from synergine.lib.process.processmanager import KeepedAliveProcessManager
from synergine.core.cycle.PipePackage import PipePackage
from synergine.core.simulation.EventManager import EventManager
from synergine.core.Signals import Signals
from synergine.synergy.event.exception.ActionAborted import ActionAborted


class CycleCalculator():
    """
    Run cycles of simulation
    """

    ACTION_RUNNED = 'signal.action_runned'

    def __init__(self, synergy_manager, force_main_process=False):
        # TODO: nbprocess
        self._synergy_manager = synergy_manager
        self._event_manager = EventManager(self._synergy_manager)
        self._event_manager.refresh()
        self._force_main_process = force_main_process
        self._process_manager = KeepedAliveProcessManager(nb_process=2, target=self._process_compute)
        self._cycle = 0
        self._current_cycle_actions_done = []

    def get_cycle(self):
        return self._cycle

    def compute(self, context):
        self._cycle += 1
        print('cycle: ', self._cycle)
        self._current_cycle_actions_done = []
        self._compute_events(context)
        return self._current_cycle_actions_done

    def _compute_events(self, context):
        for step_key, mechanisms in enumerate(self._event_manager.get_mechanisms_steps()):
            actions = self._get_computeds_objects(step_key, context)
            self._apply_actions(actions, context)
        for simulation in self._synergy_manager.get_simulations():
            simulation.end_cycle(context)

    def _get_computeds_objects(self, step_key, context):
        pipe_package = self._get_pipe_package_for_collection(step_key, context)
        if not self._force_main_process:
            computeds_objects = self._process_manager.get_their_work(pipe_package)
        else:
            pipe_package.setCountProcess(1)
            pipe_package.setCurrentProcessId(0)
            computeds_objects = self._process_compute(pipe_package)
        return computeds_objects

    def _get_pipe_package_for_collection(self, step_key, context):
        pipe_package = PipePackage()
        pipe_package.set_step_key(step_key)
        context.set_cycle(self._cycle)
        # TODO: 1: Seule les metas ont besoin d'etre trimbale
        # TODO: 2: Transporter le differentiel des metas pour le calculs a traver le reseau
        pipe_package.set_context(context)

        # TODO: Le paquet de retour contient les actions instancies. Allerger en ne transportant
        # que la liste d'acctions a fabriquer et qu'un seul
        #  exemplaire de parametres actions ?
        # import sys
        # import pickle
        # size = sys.getsizeof(pickle.dumps(pipe_package))
        # print(size)

        return pipe_package

    def _process_compute(self, pipe_package):
        """
        Since here, we are in process mode: you only have to use metas (objects_ids, states)
        :param pipe_package:
        :return:
        """
        context = pipe_package.get_context()
        step_key = pipe_package.get_step_key()
        actions = []
        for mechanism in self._event_manager.get_mechanisms_steps()[step_key]:
            mechanism_actions = mechanism.run(context)
            for mechanism_action in mechanism_actions:
                actions.append(mechanism_action)
        return actions

    def _apply_actions(self, actions, context):
        for action in actions:
            obj = self._synergy_manager.get_map().get_object(action.get_object_id())
            try:
                action.run(obj, context, self._synergy_manager)
                Signals.signal(action.__class__).send(obj=obj, context=context)
                self._current_cycle_actions_done.append(action)
            except ActionAborted:
                pass

    def end(self):
        self._process_manager.stop()