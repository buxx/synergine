from src.synergy.collection.SynergyCollection import SynergyCollection
from module.lifegame.synergy.object.Cell import Cell

class LifeGameCollection(SynergyCollection):
  
  def __init__(self):
    super(LifeGameCollection, self).__init__()
    traces = (
      (0,0,0),
      (0,1,1),
      (0,2,1),
      (0,1,2),
    )
    for i in range(4):
      cell = Cell()
      cell.addTrace(traces[i])
      self._objects.append(cell)