from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
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
    'collections' : (LifeGameCollection,) # TODO: distinction Class (et pas objet)
  },
  'connections': [TestDisplay(), CursesDisplay()],
  'test': {
    'suites' : [LifeGameTestSuite()]
  }
}