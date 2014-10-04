from src.synergy.collection.SynergyCollectionInterface import SynergyCollectionInterface
from src.synergy.object.SynergyObject import SynergyObject

class SynergyCollection(SynergyCollectionInterface):
  
  def __init__(self, configuration):
    self._configuration = configuration
    self._objects = self._configuration.getStartObjects()
  
  def getObjects(self):
    return self._objects
  
  def setObjects(self, objects):
    self._objects = objects
  
  def getComputableObjects(self):
    return self._objects
  
  def getObjectsToDisplay(self):
    
    #import pdb; pdb.set_trace()
    return self._objects
  
  def cycle(self, context):
    
    #import pdb; pdb.set_trace()
    """
    Calculs propre a la collection. Les calculs pour chaques objets
    se font ailleur (voir CycleCalculator)
    """
    for sobject in self._objects:
      pass