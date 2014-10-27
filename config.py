from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from module.lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
from module.lifegame.display.curses_visualisation import visualisation as curses_visualisation
from module.lifegame.display.pygame_visualisation import visualisation as pygame_visualisation
from synergine.src.display.CursesDisplay import CursesDisplay
from synergine.src.display.TestDisplay import TestDisplay
from synergine.src.display.PygameDisplay import PygameDisplay

config = {
    'engine': {
        'fpsmax': 25,
        'debug': {
            'mainprocess': False,
            'cycles': range(100)
        }
    },
    'simulations' : [LifeGameSimulation([LifeGameCollection(LifeGameCollectionConfiguration())])],
    'connections': [TestDisplay(), PygameDisplay(pygame_visualisation), CursesDisplay(curses_visualisation)],
    'other': {}
}