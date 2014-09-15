from src.synergy.collection.SynergyCollection import SynergyCollection
from module.lifegame.synergy.object.Cell import Cell

class LifeGameCollection(SynergyCollection):
  
  def __init__(self, configuration):
    super(LifeGameCollection, self).__init__(configuration)
    
  
  def compute(self, context):
    super(LifeGameCollection, self).compute(context)
    
    # cycle n
    # etape 1: on determine qui va mourrir  (sans les faire disparaitre)
    # etape deux: on regarde ou il va en apparaitre
    # etape 3: on retire les mourantes
    # la collection d'objet doit a se moment la representer le cycle n +1
    
    # etape 1
    cells_will_die = []
    for cell in self.getObjects():
      arround_cell_count = self._getCellCountArroundOfPosition(context, cell.getPoint())
      if arround_cell_count < 2 or arround_cell_count > 3:
        #cell.setWill('die')
        cells_will_die.append(cell)
    
    # etape 2
    for empty_point in self._getEmptyPoints():
      if not self._cellExistOnThisPoint(context, empty_point):
        #if empty_point == (0,23,20):
        #  import pdb; pdb.set_trace()
        arround_cell_count = self._getCellCountArroundOfPosition(context, empty_point)
        if arround_cell_count is 3:
          new_cell = Cell()
          new_cell.setPoint(empty_point)
          self._objects.append(new_cell)
    
    # etape 3
    for cell_die in cells_will_die:
      self._objects.remove(cell_die)
        
    # a ce stade la collection doit etre fidele
    # la map qui SERA genere aussi (mais la on ne l'utilise meme pas
    # ce qui ne peut pas marcher si on a plusieurs collections ou si
    # on passe ce self.seompte dans un sous prcess)
    
  def _getCellCountArroundOfPosition(self, context, point):
    objects_near = context.getObjectsNearPoint(point, 1)
    cell_near_count = 0
    for object_near in objects_near:
      if isinstance(object_near, Cell):
        cell_near_count += 1
    return cell_near_count
  
  def _getEmptyPoints(self):
    coordinates = []
    for x in range(100): # TODO: config ?
      for y in range(60):
        coordinates.append((0, x, y))
    return coordinates
  
  def _cellExistOnThisPoint(self, context, point):
    map = context.getMap()
    if point in map:
      for object_on_this_point in map[point]:
        if isinstance(object_on_this_point, Cell):
          return True
    return False