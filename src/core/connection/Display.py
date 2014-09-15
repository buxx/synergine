from src.core.connection.Terminal import Terminal

class Display(Terminal):
  
  def receive(self, synergy_object_manager):
    self._startOfCycle()
    for object_to_display in synergy_object_manager.getObjectsToDisplay():
      # TODO: drawObject() avec un objet generique affichable par un Display
      self.drawPoints(object_to_display.getTrace())
    self._endOfCycle()
  
  def _startOfCycle(self):
    raise NotImplementedError
  
  def _endOfCycle(self):
    raise NotImplementedError
  
  def drawPoints(self, points):
    raise NotImplementedError