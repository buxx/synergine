class DisplayConnector(object):
  
  def __init__(self, connecteds_displays):
    self._synergy_object_manager = None
    self._connecteds_displays = connecteds_displays
  
  def prepare(self, synergy_object_manager):
    self._synergy_object_manager = synergy_object_manager
  
  def cycle(self):
    if True: # Stuff est-ce que 25 fps etc
      self._sendToConnections()
  
  def _sendToConnections(self):
    # On fait tourner l'affichage avec des commandes generiques
    for object_to_display in self._getObjectsToDisplay():
      for connected_display in self._connecteds_displays:
        connected_display.drawPoints(object_to_display.getTrace())
  
  def _getObjectsToDisplay(self):
    return self._synergy_object_manager.getObjectsToDisplay()