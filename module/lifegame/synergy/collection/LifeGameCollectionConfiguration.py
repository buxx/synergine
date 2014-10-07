from src.synergy.collection.Configuration import Configuration
from module.lifegame.synergy.object.Cell import Cell

class LifeGameCollectionConfiguration(Configuration):
  
  def getStartObjects(self):
    traces = (
      #(0,0,0),
      #(0,1,0),
      #(0,0,1),
      #(0,1,1),
      #
      #(0,20,30),
      #(0,19,31),
      #(0,19,32),
      #(0,20,32),
      #(0,21,32),
      
      (0, 20, 20),
      (0, 21, 20),
      (0, 22, 20),
      (0, 22, 21),
      (0, 22, 22),
      (0, 21, 22),
      (0, 20, 22),
      
      #(0,20,20),
      #(0,21,19),
      #(0,22,19),
      #(0,22,20),
      #(0,22,21),
    )
    cells = []
    for trace in traces:
      cell = Cell()
      cell.addTrace(trace)
      cells.append(cell)
    #
    # for x in range(60):
    #   for y in range(60):
    #     cell = Cell()
    #     cell.addTrace((0, x, y))
    #     cells.append(cell)

    return cells