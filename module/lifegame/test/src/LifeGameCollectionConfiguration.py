from src.synergy.collection.Configuration import Configuration
from module.lifegame.synergy.object.Cell import Cell

class LifeGameCollectionConfiguration(Configuration):
  
  def getStartObjects(self):
    traces = (
      (0, 20, 20),
      (0, 21, 20),
      (0, 22, 20),
      (0, 22, 21),
      (0, 22, 22),
      (0, 21, 22),
      (0, 20, 22),
    )
    cells = []
    for trace in traces:
      cell = Cell()
      cell.addTrace(trace)
      cells.append(cell)
    return cells