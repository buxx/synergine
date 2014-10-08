from src.synergy.collection.SynergyCollection import SynergyCollection
from module.lifegame.synergy.event.RemoveListener import RemoveListener

class LifeGameCollection(SynergyCollection):

  def __init__(self, configuration):
    super(LifeGameCollection, self).__init__(configuration)
    self._listeners_steps = [
      [RemoveListener()]#, BornListener()]
    ]