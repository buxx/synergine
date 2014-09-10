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
  
  def compute(self, context):
    super(LifeGameCollection, self).compute()
    
    map = context.getMap()
    coordinates = []
    for x in range(100):
      for y in range(35):
        coordinates.append((0, x, y))
    for coordinate in coordinates:
      if coordinate not in map:
        count_near_cell = self.getCountCellNearCoordinate(coordinate, map)
        if count_near_cell is 3:
          #import pdb; pdb.set_trace()
          new_cell = Cell()
          new_cell.addTrace(coordinate)
          self._objects.append(new_cell)
    
    #import pdb; pdb.set_trace()
    for object in self.getObjects():
      if object.getWill() is 'die':
        self._objects.remove(object)
  
  def getCountCellNearCoordinate(self, coordinate, map):
    count_arround = 0
    arround_points = self.getArroundPointsOfPoint(coordinate)
    #import pdb; pdb.set_trace()
    for arround_point in arround_points:
      if arround_point in map:
        if isinstance(map[arround_point], Cell) or True:
          count_arround += 1
    #pdb.set_trace()
    return count_arround
  
  
  def getArroundPointsOfPoint(self, point):
    pos = point
    pz = pos[0]
    px = pos[1]
    py = pos[2]
    return (
      (pz, px-1, py-1),
      (pz, px,   py-1),
      (pz, px+1, py+1),
      (pz, px-1, py  ),
      (pz, px+1, py  ),
      (pz, px-1, py+1),
      (pz, px,   py+1),
      (pz, px+1, py-1)
    )