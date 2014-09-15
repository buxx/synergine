class Connector(object):
  # TODO: Renomme en Connector (plus de distinction pour display)
  # TODO: Connector doit devenir un lanceur d'objets connecte
  # en s'abstrayant de si c'est un affichage ou autre chose.
  # les notion de drawPoints etc devra etre de la responsabilite de l'objet de type
  # display
  # C connector lui lance aux connections a chaque cycle
  
  def __init__(self, terminals):
    self._synergy_object_manager = None
    self._terminals = terminals
  
  def prepare(self, synergy_object_manager):
    self._synergy_object_manager = synergy_object_manager
  
  def cycle(self):
    if True: # Stuff est-ce que 25 fps etc
      self._send()
  
  def _send(self):
    for terminal in self._terminals:
      terminal.receive(self._synergy_object_manager)
  
  def terminate(self):
    for terminal in self._terminals:
      terminal.terminate()
  
  def getConnectionWhoHaveToRunCore(self):
    display_who_run_core = None
    for connected_display in self._terminals:
      if connected_display.needToRunCore():
        if display_who_run_core:
          raise Exception('Two terminal try to run core. Just one can do it.')
        return connected_display
    return display_who_run_core
  
  def sendScreenToConnection(self, screen):
    display_who_run_core = self.getConnectionWhoHaveToRunCore()
    if not display_who_run_core:
      raise Exception('Need Terminal object to do that')
    display_who_run_core.initializeScreen(screen)
  