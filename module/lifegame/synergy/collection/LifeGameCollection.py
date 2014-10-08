from src.synergy.collection.SynergyCollection import SynergyCollection
from module.lifegame.synergy.event.DieListener import DieListener
from module.lifegame.synergy.event.BornListener import BornListener

class LifeGameCollection(SynergyCollection):

  def __init__(self, configuration):
    super(LifeGameCollection, self).__init__(configuration)
    self._listeners_steps = [
      [DieListener(), BornListener()]
    ]