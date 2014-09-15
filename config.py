from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
from module.lifegame.test.LifeGameTestSuite import LifeGameTestSuite
from display.TestDisplay import TestDisplay
from display.CursesDisplay import CursesDisplay

config = {
  'engine': {
    'fpsmax': 25, # 25
    'debug': {
      'mainprocess': True,
      'cycles': range(100)
    }
  },
  'simulation' : {
    'collections' : (LifeGameCollection(LifeGameCollectionConfiguration()),)
  },
  'connections': [TestDisplay(), CursesDisplay()],
  'test': {
    'suites' : [LifeGameTestSuite()]
  }
}