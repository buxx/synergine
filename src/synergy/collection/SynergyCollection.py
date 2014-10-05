from src.synergy.collection.SynergyCollectionInterface import SynergyCollectionInterface
from src.synergy.object.SynergyObject import SynergyObject

class SynergyCollection(SynergyCollectionInterface):
  
  def __init__(self, configuration, simulation):
    self._configuration = configuration
    self._simulation = simulation
    self._objects = self._configuration.getStartObjects()

  def getObjects(self):
    return self._objects
  
  def setObjects(self, objects):
    self._objects = objects

  def getSimulation(self):
    return self._simulation

  def getComputableObjects(self):
    return self._objects
  
  def getObjectsToDisplay(self):
    
    #import pdb; pdb.set_trace()
    return self._objects
