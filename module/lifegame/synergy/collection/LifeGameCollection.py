from src.synergy.collection.SynergyCollection import SynergyCollection
from module.lifegame.synergy.event.DieListener import DieListener
from module.lifegame.synergy.event.BornListener import BornListener

class LifeGameCollection(SynergyCollection):

  def __init__(self, configuration):
    super(LifeGameCollection, self).__init__(configuration)
    self._listeners_steps = [
      [DieListener, BornListener]
    ]

  def getObjectsToDisplay(self):
    objects_to_display = []
    for obj in self._objects:
      if obj.is_alive():
        objects_to_display.append(obj)
    return objects_to_display