from src.synergy.object.SynergyObjectInterface import SynergyObjectInterface

class SynergyObject(SynergyObjectInterface):
  
  def __init__(self, ):
    self._cycle_frequency = 1
    # TODO: Cet histoire de trace est trop dependante d'objet a trace
    self._trace_length = 1
    self._trace = []
    self._will = None
  
  def getWill(self):
    return self._will
  
  # TODO: Gestion space dtata autrement ?
  def addTrace(self, point):
    # TODO: limite de taille de trace
    self._trace.append(point)
  
  def getTrace(self):
    return self._trace
  
  # TODO: qui execute le calcul du cycle ? Utiliser les objets de la simulation
  # le chergerai de trop de responsabilite ?
  def cycle(self, context):
    pass