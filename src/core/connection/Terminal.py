class Terminal():

  def __init__(self):
    self._encapsuled_run = False

  def encapsulate_run(self, run_function):
    self._encapsuled_run = True

  def haveEncapsulatedRun(self):
    return self._encapsuled_run
  
  def needToRunCore(self):
    return False
  
  # TODO: Renommer
  def initializeScreen(self, screen):
    pass
  
  def receive(self, synergy_object_manager):
    pass
  
  def terminate(self):
    pass