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
