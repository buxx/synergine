from src.synergy.collection.SynergyCollection import SynergyCollection
from module.lifegame.synergy.object.Cell import Cell

class LifeGameCollection(SynergyCollection):
  
  def __init__(self):
    super(LifeGameCollection, self).__init__()
    traces = (
      (0,20,30),
      (0,19,31),
      (0,19,32),
      (0,20,32),
      (0,21,32),
      
      (0,20,20),
      (0,21,19),
      (0,22,19),
      (0,22,20),
      (0,22,21),
    )
    for i in range(10):
      cell = Cell()
      cell.addTrace(traces[i])
      self._objects.append(cell)
  
  def compute(self, context):
    super(LifeGameCollection, self).compute()
    
    # cycle n
    # etape 1: on determine qui va mourrir  (sans les faire disparaitre)
    # etape deux: on regarde ou il va en apparaitre
    # etape 3: on retire les mourantes
    # la collection d'objet doit a se moment la representer le cycle n +1
    
    # etape 1
    cells_will_die = []
    for cell in self.getObjects():
      arround_cell = self._getCellArroundOfPosition(cell.getPoint())
      if arround_cell < 2 or arround_cell > 3:
        cell.setWill('die')
        cell_will_die.append(cell)
    
    # etape 2
    for empty_point in self._getEmptyPoints():
      if not self._cellExistOnThisPoint():
        arround_cell = self._getCellArroundOfPosition(cell.getPoint())
        if arround_cell is 3:
          new_cell = Cell()
          new_cell.setPoint(empty_point)
    
    # etape 3
    for cell_die in cells_will_die:
      self._objects.remove(cell_die)
    
    # a ce stade la collection doit etre fidele
    # la map qui SERA genere aussi (mais la on ne l'utilise meme pas
    # ce qui ne peut pas marcher si on a plusieurs collections ou si
    # on passe ce self.seompte dans un sous prcess)
    
    
    pass
    
    
    ## Reecriture !!!
    map = context.getMap()
    
    
    
    coordinates = []
    for x in range(100):
      for y in range(35):
        coordinates.append((0, x, y))
    for coordinate in coordinates:
      if coordinate not in map:
        #if coordinate == (0, 21, 20):
        #  import pdb; pdb.set_trace()
        count_near_cell = self.getCountCellNearCoordinate(coordinate, map)
        if count_near_cell is 3:
          #import pdb; pdb.set_trace()
          new_cell = Cell()
          new_cell.addTrace(coordinate)
          print('new at', coordinate)
          self._objects.append(new_cell)
      
    
    #import pdb; pdb.set_trace()
    for object in self.getObjects():
      if object.getWill() is 'die':
        print('remove', object)
        self._objects.remove(object)
        # remove from map
        #if object.getPoint() == (0,22,19):
        #import pdb; pdb.set_trace()
        map[object.getPoint()].remove(object)
        if len(map[object.getPoint()]) == 0:
          del(map[object.getPoint()])
      
  
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