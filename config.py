from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from display.TestDisplay import TestDisplay

config = {
  'engine': {
    'fpsmax': 25
  },
  'simulation' : {
    'collections' : (LifeGameCollection,)
  },
  'display': {
    'displays': [TestDisplay]
  }
}