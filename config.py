from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from display.TestDisplay import TestDisplay
from display.CursesDisplay import CursesDisplay

config = {
  'engine': {
    'fpsmax': 3, # 25
    'debug': {
      'mainprocess': True
    }
  },
  'simulation' : {
    'collections' : (LifeGameCollection,)
  },
  'display': {
    'displays': [TestDisplay, CursesDisplay]
  }
}