from src.synergy.collection.SynergyCollectionInterface import SynergyCollectionInterface
from src.synergy.object.SynergyObject import SynergyObject

class SynergyCollection(SynergyCollectionInterface):
  
  def __init__(self):
    self._objects = []
  
  def getObjects(self):
    return self._objects
  
  def setObjects(self, objects):
    self._objects = objects
  
  def getComputableObjects(self):
    return self._objects
  
  def getObjectsToDisplay(self):
    
    #import pdb; pdb.set_trace()
    return self._objects
  
  def compute(self, context):
    
    #import pdb; pdb.set_trace()
    """
    Calculs propre a la collection. Les calculs pour chaques objets
    se font ailleur (voir CycleCalculator)
    """
    for sobject in self._objects:
      pass