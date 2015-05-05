from synergine.synergy.collection.SynergyCollection import SynergyCollection
from lifegame.synergy.event.DieAction import DieAction
from lifegame.synergy.event.BornAction import BornAction
from lifegame.synergy.event.TimePassAction import TimePassAction


class LifeGameCollection(SynergyCollection):

    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [DieAction, BornAction, TimePassAction]
