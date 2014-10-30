from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from module.lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
from module.lifegame.display.curses_visualisation import visualisation as curses_visualisation
from module.lifegame.display.pygame_visualisation import visualisation as pygame_visualisation
from synergine.src.display.CursesDisplay import CursesDisplay
from synergine.src.display.TestDisplay import TestDisplay
from synergine.src.display.PygameDisplay import PygameDisplay

config = {
    'app': {
        'name': 'Synergine'
    },
    'engine': {
        'fpsmax': 25,
        'debug': {
            'mainprocess': False,
            'cycles': range(100)
        }
    },
    'simulations' : [LifeGameSimulation([LifeGameCollection(LifeGameCollectionConfiguration())])],
    'connections': [TestDisplay, PygameDisplay, CursesDisplay],
    'terminal': {
        '__default__': {
            'app': {
                'name': 'Synergine (graphic output)'
            },
            'display': {
                'grid': {
                    'size': 20
                }
            }
        },
        'pygame': {
            'visualisation': pygame_visualisation,
            'window_size': (800, 600),
            'app': {
                'name': 'Synergine (pygame)'
            },
            'font': {
                'name': 'arial',
                'size': 13
            }
        },
        'curses': {
            'visualisation': curses_visualisation,
            'display': {
                'grid': {
                    'size': 1
                }
            }
        }
    }
}