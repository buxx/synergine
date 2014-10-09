from src.synergy.collection.SynergyCollectionInterface import SynergyCollectionInterface
from src.synergy.object.SynergyObject import SynergyObject

class SynergyCollection(SynergyCollectionInterface):
  
  def __init__(self, configuration):
    self._configuration = configuration
    self._objects = self._configuration.getStartObjects()
    self._actions_steps = [[]]

  def get_actions_steps(self):
    return self._actions_steps

  def getObjects(self):
    return self._objects
  
  def setObjects(self, objects):
    self._objects = objects

  def remove_object(self, object):
    self._objects.remove(object)

  def get_object_by_key(self, key):
    return self._objects[key]

  def getComputableObjects(self):
    return self._objects
  
  def getObjectsToDisplay(self):
    
    #import pdb; pdb.set_trace()
    return self._objects
