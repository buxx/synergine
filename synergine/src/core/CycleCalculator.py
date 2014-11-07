from synergine.lib.process.processmanager import KeepedAliveProcessManager
from synergine.src.core.cycle.PipePackage import PipePackage
from synergine.src.core.simulation.EventManager import EventManager

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

    def compute(self, context):
        self._cycle += 1
        self._compute_events(context)

    def _compute_events(self, context):
        for simulation in context.get_simulations():
            simulation.start_cycle(context)
            collections = simulation.get_collections()
            for collection in collections:#context.get_collections():
                for collection_mechanisms_step in self._event_manager.get_collection_mechanisms_steps(collection):
                    computeds_objects = self._get_computeds_objects(collection, collection_mechanisms_step, context)
                    collection.set_objects(computeds_objects)
                    # TODO: actions toutes d'un coups apres le trait des col non ?
                    self._apply_actions(computeds_objects, collection, context)
            simulation.end_cycle(context)

    def _get_computeds_objects(self, collection, collection_mechanisms_step, context):
        pipe_package = self._get_pipe_package_for_collection(collection.get_computable_objects(), collection_mechanisms_step, context)
        if not self._force_main_process:
            computeds_objects = self._process_manager.get_their_work(pipe_package)
        else:
            computeds_objects = self._process_compute(pipe_package)
        return computeds_objects

    def _get_pipe_package_for_collection(self, objects, mechanisms, context):
        # FUTURE: test si garder le package en attribut de core ameliore les perfs (attention a l'index de current_process)
        pipe_package = PipePackage(objects)
        pipe_package.set_mechanisms(mechanisms)
        pipe_package.set_context(context)
        return pipe_package

    def _process_compute(self, pipe_package):
        objects_to_compute = pipe_package.getChunkedObjects()
        context = pipe_package.get_context()
        mechanisms = pipe_package.get_mechanisms()
        for mechanism in mechanisms:
            mechanism.run(objects_to_compute, context)
        return objects_to_compute

    def _apply_actions(self, objects, collection, context):
        actions = []
        # On prepare une liste d'actions au lieu d'iterer directement sur les object. Afin d'eviter les problemes
        # du au fait d'iterer sur une liste d'objet susceptible d'etre modifie (suppression)
        for obj in objects:
            action = obj.get_will()
            if action:
                # On reconstruit une liste d'actions auxquel on redonne les objets. On doit faire cela car
                # si l'on donne les objets aux actions avant ils peuvent etre donne dans un process
                # (autre obj en memoire)
                action.set_object(obj)
                actions.append(action)
                obj.set_will(None)
        for action in actions:
            action.run(collection, context)
        for obj in objects:
            obj.end_cycle()

    def end(self):
        self._process_manager.stop()