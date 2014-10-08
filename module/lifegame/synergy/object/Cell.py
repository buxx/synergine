from src.synergy.object.SynergyObject import SynergyObject

class Cell(SynergyObject):

  def __init__(self):
    super(Cell, self).__init__()
    self._alive = False

  def addTrace(self, point):
    """
    Cell have only one point length
    """
    self._trace = [point]
  
  def setPoint(self, point):
    self.addTrace(point)
  
  def getPoint(self):
    return self.getTrace()[0]

  def set_alive(self, alive):
    self._alive = alive

  def is_alive(self):
    return self._alive