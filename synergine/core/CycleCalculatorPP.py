from synergine.lib.process.processmanager import KeepedAliveProcessManager
from synergine.core.cycle.PipePackage import PipePackage
from synergine.core.simulation.EventManager import EventManager
<<<<<<< Updated upstream
=======
from synergine.core.Signals import Signals
from synergine.synergy.event.exception.ActionAborted import ActionAborted
>>>>>>> Stashed changes


class CycleCalculator():
    """
    Run cycles of simulation
    """

    def __init__(self, synergy_manager, force_main_process = False):
        # TODO: nbprocess
        self._synergy_manager = synergy_manager
        self._event_manager = EventManager()
        self._event_manager.refresh(self._synergy_manager.get_collections())
        self._force_main_process = force_main_process
        self._process_manager = KeepedAliveProcessManager(nb_process=2, target=self._process_compute)
        self._cycle = 0

    def get_cycle(self):
      return self._cycle

    def compute(self, context):
        self._cycle += 1
        self._compute_events(context)

    def _compute_events(self, context):
        for simulation in self._synergy_manager.get_simulations():
            simulation.start_cycle(context)
            collections = simulation.get_collections()
            for collection in collections:#context.get_collections():
                collection_mechanisms_steps = self._event_manager.get_collection_mechanisms_steps(collection)
                for collection_mechanisms_step in self._event_manager.get_collection_mechanisms_steps(collection):
                    # TODO: (run test) tte les actions d'un coup
                    # On peux donner collection et contexte a l'action ? Le process va t-il dupliquer ces objets ?
                    # TODO: On cherche a readonly/share les objects. Mais le contexte aussi  peut être en ReadOnly
                    actions = self._get_computeds_objects(collection, collection_mechanisms_step, context)
                    self._apply_actions(actions, collection, context)
            simulation.end_cycle(context)

    def _get_computeds_objects(self, collection, collection_mechanisms_step, context):
        pipe_package = self._get_pipe_package_for_collection(collection.get_computable_objects(), collection_mechanisms_step, context)
        if not self._force_main_process:
            computeds_objects = self._process_manager.get_their_work(pipe_package)
        else:
            computeds_objects = self._process_compute(pipe_package)
        return computeds_objects

    def _get_pipe_package_for_collection(self, objects, mechanisms, context):
        # TODO: FUTURE: test si garder le package en attribut de core ameliore les perfs (attention a l'index de current_process)
        # TODO: Le package transporte les ids de tout les objets dans les processus. C'est inutile.
        pipe_package = PipePackage([obj.get_id() for obj in objects])
        pipe_package.set_mechanisms(mechanisms)
        context.set_cycle(self._cycle)
        pipe_package.set_context(context)

        # TODO: Le paquet de retour contient les actions instancies. Allerger en ne transportant
        # que la liste d'acctions a fabriquer et qu'un seul
        # exemplaire de parametres actions ?
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
        objects_ids_to_compute = pipe_package.getChunkedObjects()
        context = pipe_package.get_context()

        mechanisms = pipe_package.get_mechanisms()
        actions = []
        for mechanism in mechanisms:
            mechanism_actions = mechanism.run(objects_ids_to_compute, context)
            for mechanism_action in mechanism_actions:
                actions.append(mechanism_action)
        return actions

    def _apply_actions(self, actions, collection, context):
        for action in actions:
            obj = self._synergy_manager.get_map().get_object(action.get_object_id())
<<<<<<< Updated upstream
            action.run(obj, collection, context, self._synergy_manager)
=======
            try:
                action.run(obj, collection, context, self._synergy_manager)
                Signals.signal(action.__class__).send(obj=obj, context=context)
            except ActionAborted:
                pass
>>>>>>> Stashed changes

    def end(self):
        self._process_manager.stop()