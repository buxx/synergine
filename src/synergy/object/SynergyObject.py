from src.synergy.object.SynergyObjectInterface import SynergyObjectInterface

class SynergyObject(SynergyObjectInterface):
  
  def __init__(self):
    self._cycle_frequency = 1
    # TODO: Cet histoire de trace est trop dependante d'objet a trace
    self._trace_length = 1
    self._trace = []
    self._will = None
  
  def setWill(self, action):
    self._will = action
  
  def getWill(self):
    return self._will
  
  # TODO: Gestion space dtata autrement ?
  def addTrace(self, point):
    # TODO: limite de taille de trace
    self._trace.append(point)
  
  def getTrace(self):
    return self._trace
