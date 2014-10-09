from src.synergy.collection.SynergyCollection import SynergyCollection
from module.lifegame.synergy.event.DieAction import DieAction
from module.lifegame.synergy.event.BornAction import BornAction

class LifeGameCollection(SynergyCollection):

  def __init__(self, configuration):
    super().__init__(configuration)
    self._actions_steps = [
      [DieAction, BornAction]
    ]

  def getObjectsToDisplay(self):
    objects_to_display = []
    for obj in self._objects:
      if obj.is_alive():
        objects_to_display.append(obj)
    return objects_to_display