from lib.process.processmanager import KeepedAliveProcessManager
# TODO: tmp ...
from os import getpid

class CycleCalculator(object):
  
  def __init__(self):
    # TODO: nbprocess
    self._process_manager = KeepedAliveProcessManager(nb_process=2, target=self._process_compute)
  
  def compute(self, objects):
    self._process_manager.get_their_work(objects)
  
  def _process_compute(self, objects):
    for object in objects:
      print(getpid(), object)
      
  def end(self):
    self._process_manager.stop()