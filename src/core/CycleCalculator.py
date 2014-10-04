from lib.process.processmanager import KeepedAliveProcessManager
from src.core.cycle.PipePackage import PipePackage

class CycleCalculator(object):
  
  def __init__(self, force_main_process = False):
    # TODO: nbprocess
    self._force_main_process = force_main_process
    self._process_manager = KeepedAliveProcessManager(nb_process=2, target=self._process_compute)
  
  def compute(self, context):
    collections = context.getCollections()
    for collection in collections:
      pipe_package = self._getPipePackageForCollection(collection, context)
      if not self._force_main_process:
        computeds_objects = self._process_manager.get_their_work(pipe_package)
      else:
        computeds_objects = self._process_compute(pipe_package)
      collection.setObjects(computeds_objects)
      
    for collection in collections:
      collection.cycle(context)
  
  def _getPipePackageForCollection(self, collection, context):
    # FUTURE: test si garder le package en attribut de core ameliore les perfs (attention a l'index de current_process)
    pipe_package = PipePackage(collection.getComputableObjects())
    pipe_package.setContext(context)
    return pipe_package
  
  def _process_compute(self, pipe_package):
    objects_to_compute = pipe_package.getChunkedObjects()
    for obj in objects_to_compute:
      obj.cycle(pipe_package.getContext())
    return objects_to_compute
      
  def end(self):
    self._process_manager.stop()