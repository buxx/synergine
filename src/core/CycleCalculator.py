from lib.process.processmanager import KeepedAliveProcessManager
from src.core.cycle.PipePackage import PipePackage
from src.core.simulation.EventManager import EventManager

class CycleCalculator(object):
  
  def __init__(self, synergy_manager, force_main_process = False):
    # TODO: nbprocess
    self._synergy_manager = synergy_manager
    self._object_event_manager = EventManager()
    self._object_event_manager.refresh(self._synergy_manager.getObjectListeners())
    self._global_event_manager = EventManager()
    self._global_event_manager.refresh(self._synergy_manager.getGlobalListeners())
    self._force_main_process = force_main_process
    self._process_manager = KeepedAliveProcessManager(nb_process=2, target=self._process_compute)
  
  def compute(self, context):
    # TODO: Reflechir a la pertinence de permettre x cycles avant l'application des actions
    self._compute_object(context)
    self._compute_global(context)
    self._apply_actions(context)

  def _compute_object(self, context):
    for simulation in context.getSimulations():
      collections = simulation.getCollections()
      for collection in collections:
        pipe_package = self._getPipePackageForCollection(simulation, collection, context)
        if not self._force_main_process:
          computeds_objects = self._process_manager.get_their_work(pipe_package)
        else:
          computeds_objects = self._process_compute(pipe_package)
        collection.setObjects(computeds_objects)

  def _compute_global(self, context):
    # TODO: Dans sous process ?
    mechanisms = self._global_event_manager.get_mechanisms()
    for mechanism in mechanisms:
      mechanism.run(context.getObjects(), context)

  def _apply_actions(self, context):
    # TODO: doit devenir une simple execution des actions
    for simulation in context.getSimulations():
      collections = simulation.getCollections()
      for collection in collections:
        simulation.run_collection_cycle(collection, context)  # doit disparaitre
      simulation.run_simulation_cycle(context)  # doit disparaitre

  def _getPipePackageForCollection(self, simulation, collection, context):
    # FUTURE: test si garder le package en attribut de core ameliore les perfs (attention a l'index de current_process)
    pipe_package = PipePackage(collection.getComputableObjects())
    pipe_package.setContext(context)
    pipe_package.setCurrentSimulation(simulation)
    return pipe_package
  
  def _process_compute(self, pipe_package):
    objects_to_compute = pipe_package.getChunkedObjects()
    context = pipe_package.getContext()
    mechanisms = self._object_event_manager.get_mechanisms()
    for mechanism in mechanisms:
      mechanism.run(objects_to_compute, context)

      #mechanisms_objects = mechanism.get_concerned_objects(objects_to_compute)
      #for mechanisms_object in mechanisms_objects:
      #  mechanism.run(mechanisms_object, context)

    for obj in objects_to_compute:
      simulation = pipe_package.getCurrentSimulation()
      simulation.run_object_cycle(obj, context)
    return objects_to_compute
      
  def end(self):
    self._process_manager.stop()