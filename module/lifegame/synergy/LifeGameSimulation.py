from src.synergy.Simulation import Simulation
from module.lifegame.synergy.object.Cell import Cell

class LifeGameSimulation(Simulation):

  def run_object_cycle(self, obj, context):
    objects_near = context.getObjectsNearPoint(obj.getPoint(), 1)
    cell_near_count = 0
    for object_near in objects_near:
      if isinstance(object_near, Cell):
        cell_near_count += 1
    if cell_near_count < 2 or cell_near_count > 3:
      obj.setWill('die')

  def run_collection_cycle(self, collection, context):

    for empty_point in self._getEmptyPoints():
      if not self._cellExistOnThisPoint(context, empty_point):
        arround_cell_count = self._getCellCountArroundOfPosition(context, empty_point)
        if arround_cell_count is 3:
          new_cell = Cell()
          new_cell.setPoint(empty_point)
          collection._objects.append(new_cell)  # TODO: addObject sur collection

    # etape 3
    new_objects_col = []
    for cell in collection.getObjects():
      if cell.getWill() != 'die':
        new_objects_col.append(cell)
      else:
        del(cell)
    collection._objects = new_objects_col  # TODO: setObjects sur collection

  def _getCellCountArroundOfPosition(self, context, point):
    objects_near = context.getObjectsNearPoint(point, 1)
    cell_near_count = 0
    for object_near in objects_near:
      if isinstance(object_near, Cell):
        cell_near_count += 1
    return cell_near_count

  def _getEmptyPoints(self):
    # TODO: Optimiser en ne creant les empty point (faire un carre x+1 y+1 des cell les plus loins ?)
    coordinates = []
    for x in range(100): # TODO: Le calcul ne doit pas depasser la taille du monde.
      # et la taille du monde doit etre gere qqpart
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

  def run_simulation_cycle(self, context):
    pass