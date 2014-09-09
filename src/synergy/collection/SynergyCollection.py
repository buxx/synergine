from src.synergy.collection.SynergyCollectionInterface import SynergyCollectionInterface
from src.synergy.object.SynergyObject import SynergyObject

class SynergyCollection(SynergyCollectionInterface):
  
  def __init__(self):
    super(SynergyCollection, self).__init__()
    for i in range(20):
      self._objects.append(SynergyObject())
  
  def getComputableObjects(self):
    return self._objects
  
  def compute(self):
    """
    Calculs propre a la collection. Les calculs pour chaques objets
    se font ailleur (voir CycleCalculator)
    """
    print(len(self._objects))