from src.synergy.collection.Configuration import Configuration
from module.lifegame.synergy.object.Cell import Cell

class LifeGameCollectionConfiguration(Configuration):
  
  def getStartObjects(self):
    cells = []
    # cell grid
    for x in range(40):
      for y in range(50):
        cell = Cell()
        cell.addTrace((0, x, y))
        cells.append(cell)

    alive_cell_traces = (
      (0, 20, 20),
      (0, 21, 20),
      (0, 22, 20),
      (0, 22, 21),
      (0, 22, 22),
      (0, 21, 22),
      (0, 20, 22)
    )
    for dead_cell in cells:
      if cell.getPoint() in alive_cell_traces:
        cell.set_alive(True)

    return cells