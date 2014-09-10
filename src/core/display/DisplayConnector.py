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
    for connected_display in self._connecteds_displays:
      for object_to_display in self._getObjectsToDisplay():
        connected_display.drawPoints(object_to_display.getTrace())
      connected_display.endOfCycle()
  
  def _getObjectsToDisplay(self):
    return self._synergy_object_manager.getObjectsToDisplay()
  
  def terminate(self):
    for connected_display in self._connecteds_displays:
      connected_display.terminate()
  
  def getDisplayWhoHaveToRunCore(self):
    display_who_run_core = None
    for connected_display in self._connecteds_displays:
      if connected_display.needToRunDisplay():
        if display_who_run_core:
          raise Exception('Two display try to run core. Just one can do it.')
        return connected_display
    return display_who_run_core
  
  def sendScreenToDisplay(self, screen):
    display_who_run_core = self.getDisplayWhoHaveToRunCore()
    if not display_who_run_core:
      raise Exception('Need Display object to do that')
    display_who_run_core.initializeScreen(screen)
  