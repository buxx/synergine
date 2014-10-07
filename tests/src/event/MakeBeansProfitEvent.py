from src.synergy.event.Event import Event
from tests.src.TestSynergyObject import TestSynergyObject

class MakeBeansProfitEvent(Event):

  def __init__(self, listeners):
    super(MakeBeansProfitEvent, self).__init__(listeners)
    self._concerneds = [TestSynergyObject]