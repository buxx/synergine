from synergine.synergy.collection.SynergyCollection import SynergyCollection
from lifegame.synergy.event.DieAction import DieAction
from lifegame.synergy.event.BornAction import BornAction
from lifegame.synergy.event.TimePassAction import TimePassAction


class LifeGameCollection(SynergyCollection):
    """
    This collection own cells of simulation.
    """

    def __init__(self, configuration):
        super().__init__(configuration)
        # We list here actions who concern our simulation.
        self._actions = [DieAction, BornAction, TimePassAction]
