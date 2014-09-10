class Display(object):
  
  def encapsulate_run(self):
    pass
  
  def needToRunDisplay(self):
    return False
  
  def initializeScreen(self, screen):
    pass
  
  def endOfCycle(self):
    raise NotImplementedError
  
  def terminate(self):
    raise NotImplementedError
  
  def drawPoints(self, points):
    raise NotImplementedError