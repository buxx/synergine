from synergine.src.synergy.collection.SynergyCollection import SynergyCollection
from module.lifegame.synergy.event.DieAction import DieAction
from module.lifegame.synergy.event.BornAction import BornAction


class LifeGameCollection(SynergyCollection):

    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [DieAction, BornAction]

    def get_objects_to_display(self) -> list:
        objects_to_display = []
        for obj in self._objects:
            if obj.is_alive() or obj.get_is_died_since() <= 2:
                objects_to_display.append(obj)
        return objects_to_display