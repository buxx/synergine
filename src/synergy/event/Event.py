from src.synergy.object import SynergyObject
from src.core.simulation.mechanism.Mechanism import Mechanism

class Event(object):

  def __init__(self, listeners):
    self._listeners = listeners
    self._mechanism = Mechanism
    self._concerneds = [SynergyObject]

  def getMechanismClass(self):
    return self._mechanism

  def observe(self, obj, context, parameters={}):
    if self._object_match(obj, context, parameters):
      for listener in self._listeners:
        obj.setWill(listener(parameters))

  def _object_match(self, obj, context, parameters={}):
    for concerned in self._concerneds:
      if isinstance(obj, concerned):
        return True
    return False