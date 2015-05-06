from lifegame.PrintTerminal import PrintTerminal
from lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
from lifegame.display.curses_visualisation import visualisation as curses_visualisation
from lifegame.display.pygame_visualisation import visualisation as pygame_visualisation
from xyworld.display.CursesDisplay import CursesDisplay
from xyworld.display.PygameDisplay import PygameDisplay
from synergine.display.TestDisplay import TestDisplay
from xyzworld.Context import Context as XyzContext

config = {
    'app': {
        'name': 'Synergine',
        'classes': {
          'Context': XyzContext
        }
    },
    'engine': {
        'fpsmax': 255,
        'debug': {
            'mainprocess': False,
            'cycles': 100
        }
    },
    'simulations': [LifeGameSimulation([LifeGameCollection(LifeGameCollectionConfiguration())])],
    'connections': [PrintTerminal],#, TestDisplay, PygameDisplay],#, CursesDisplay],
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
            },
            'background': {
              'color': (0, 0, 0)
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
