from src.synergy.collection.SynergyCollection import SynergyCollection
from module.lifegame.synergy.object.Cell import Cell

class LifeGameCollection(SynergyCollection):
  
  def __init__(self):
    super(LifeGameCollection, self).__init__()
    for i in range(10):
      cell = Cell()
      cell.addTrace((0, i, i))
      self._objects.append(cell)