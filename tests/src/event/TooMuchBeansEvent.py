from src.synergy.event.Event import Event
from tests.src.TestSynergyObject import TestSynergyObject

class TooMuchBeansEvent(Event):

  def __init__(self, actions):
    super().__init__(actions)
    self._concerneds = [TestSynergyObject]

  def _object_match(self, obj, context, parameters={}):
    if super()._object_match(obj, context, parameters):
      if obj.beans > 10000000:
        return True
    return False
