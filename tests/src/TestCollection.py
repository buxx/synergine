from synergine.synergy.collection.SynergyCollection import SynergyCollection
from tests.src.event.TooMuchBeansAction import TooMuchBeansAction
from tests.src.event.MakeBeansProfitAction import MakeBeansProfitAction
from tests.src.event.LonelinessSuicideAction import LonelinessSuicideAction

class TestCollection(SynergyCollection):

    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [MakeBeansProfitAction, TooMuchBeansAction, LonelinessSuicideAction]
