class SynergyObjectInterface(object):
  
  def __init__(self):
    self._cycle_frequency = 1
  
  def think(self):
    raise NotImplementedError()