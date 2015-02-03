from synergine.synergy.collection.SynergyCollection import SynergyCollection
from lifegame.synergy.event.DieAction import DieAction
from lifegame.synergy.event.BornAction import BornAction
from lifegame.synergy.event.TimePassAction import TimePassAction


class LifeGameCollection(SynergyCollection):

    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [DieAction, BornAction, TimePassAction]

    def get_objects_to_display(self) -> list:
        objects_to_display = []
        return self._objects
        for obj in self._objects:
            if obj.is_alive() or obj.get_is_died_since() <= 2:
                objects_to_display.append(obj)
        return objects_to_display