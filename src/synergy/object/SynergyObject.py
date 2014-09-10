from src.synergy.object.SynergyObjectInterface import SynergyObjectInterface

class SynergyObject(SynergyObjectInterface):
  
  def __init__(self):
    self._cycle_frequency = 1
    self._trace = []
  
  # TODO: Gestion space dtata autrement ?
  def addTrace(self, point):
    self._trace.append(point)
  
  def getTrace(self):
    return self._trace
  
  # TODO: qui execute le calcul du cycle ? Utiliser les objets de la simulation
  # le chergerai de trop de responsabilite
  def cycle(self):
    pass