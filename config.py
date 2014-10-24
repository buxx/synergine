from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from module.lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
from synergine.display.TestDisplay import TestDisplay
from synergine.display.CursesDisplay import CursesDisplay
from synergine.display.PygameDisplay import PygameDisplay
from module.lifegame.curses.default_visualisation import visualisation

config = {
    'engine': {
        'fpsmax': 25,
        'debug': {
            'mainprocess': False,
            'cycles': range(100)
        }
    },
    'simulations' : [LifeGameSimulation([LifeGameCollection(LifeGameCollectionConfiguration())])],
    'connections': [TestDisplay(), PygameDisplay(), CursesDisplay(visualisation)],
    'other': {
        'action_manager': {
            'max_recursions': 1000
        }
    }
}