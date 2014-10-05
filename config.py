from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from module.lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
from display.TestDisplay import TestDisplay
from display.CursesDisplay import CursesDisplay

config = {
  'engine': {
    'fpsmax': 25, # 25
    'debug': {
      'mainprocess': False,
      'cycles': range(100)
    }
  },
  'simulations' : [LifeGameSimulation([LifeGameCollection(LifeGameCollectionConfiguration())])],
  'connections': [TestDisplay(), CursesDisplay()],
}