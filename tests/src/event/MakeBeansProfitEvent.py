from src.synergy.event.Event import Event
from tests.src.TestSynergyObject import TestSynergyObject

class MakeBeansProfitEvent(Event):

    def __init__(self, actions):
        super().__init__(actions)
        self._concerneds = [TestSynergyObject]