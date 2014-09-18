from src.synergy.object.SynergyObject import SynergyObject

class Cell(SynergyObject):
  
  def addTrace(self, point):
    """
    Cell have only one point length
    """
    self._trace = [point]
  
  def setPoint(self, point):
    self.addTrace(point)
  
  def getPoint(self):
    return self.getTrace()[0]
  
  def cycle(self, context):
    objects_near = context.getObjectsNearPoint(self.getPoint(), 1)
    cell_near_count = 0
    for object_near in objects_near:
      if isinstance(object_near, Cell):
        cell_near_count += 1
    if cell_near_count < 2 or cell_near_count > 3:
      self.setWill('die')