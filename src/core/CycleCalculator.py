from lib.process.processmanager import KeepedAliveProcessManager

# TODO: tmp ...
from os import getpid

class CycleCalculator(object):
  
  def __init__(self, force_main_process = False):
    # TODO: nbprocess
    self._force_main_process = force_main_process
    self._process_manager = KeepedAliveProcessManager(nb_process=2, target=self._process_compute)
  
  def compute(self, pipe_package):
    if not self._force_main_process:
      return self._process_manager.get_their_work(pipe_package)
    return self._process_compute(pipe_package)
  
  def _process_compute(self, pipe_package):
    # TODO: Ici le package nous donne des trucs a jours depuis le process a jour
    map = pipe_package.getMap()
    objects_to_compute = pipe_package.getChunkedObjects()
    for object in objects_to_compute:
      object.think()
      print(getpid(), object)
    return objects_to_compute
      
  def end(self):
    self._process_manager.stop()