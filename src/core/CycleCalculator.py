from lib.process.processmanager import KeepedAliveProcessManager
from src.core.cycle.PipePackage import PipePackage
from src.core.simulation.EventManager import EventManager

class CycleCalculator(object):
  
  def __init__(self, synergy_manager, force_main_process = False):
    # TODO: nbprocess
    self._synergy_manager = synergy_manager
    self._event_manager = EventManager()
    self._event_manager.refresh(self._synergy_manager.getCollections())
    self._force_main_process = force_main_process
    self._process_manager = KeepedAliveProcessManager(nb_process=2, target=self._process_compute)
  
  def compute(self, context):
    # TODO: Reflechir a la pertinence de permettre x cycles avant l'application des actions
    self._compute_events(context)
    self._apply_actions(context)

  def _compute_events(self, context):
    for simulation in context.getSimulations():
      collections = simulation.getCollections()
      for collection in collections:#context.getCollections():
        for collection_mechanisms_step in self._event_manager.get_collection_mechanisms_steps(collection):
          pipe_package = self._getPipePackageForCollection(collection.getComputableObjects(), collection_mechanisms_step, context)
          if not self._force_main_process:
            computeds_objects = self._process_manager.get_their_work(pipe_package)
          else:
            computeds_objects = self._process_compute(pipe_package)
          collection.setObjects(computeds_objects)

  def _getPipePackageForCollection(self, objects, mechanisms, context):
    # FUTURE: test si garder le package en attribut de core ameliore les perfs (attention a l'index de current_process)
    pipe_package = PipePackage(objects)
    pipe_package.setMechanisms(mechanisms)
    pipe_package.setContext(context)
    return pipe_package

  def _process_compute(self, pipe_package):
    objects_to_compute = pipe_package.getChunkedObjects()
    context = pipe_package.getContext()
    mechanisms = pipe_package.getMechanisms()
    for mechanism in mechanisms:
      mechanism.run(objects_to_compute, context)
    return objects_to_compute

  def _apply_actions(self, context):
    # TODO: doit devenir une simple execution des actions
    for simulation in context.getSimulations():
      collections = simulation.getCollections()
      for collection in collections:
        simulation.run_collection_cycle(collection, context)  # doit disparaitre
      simulation.run_simulation_cycle(context)  # doit disparaitre
      
  def end(self):
    self._process_manager.stop()