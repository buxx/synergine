from lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
from lifegame.display.curses_visualisation import visualisation as curses_visualisation
from lifegame.display.pygame_visualisation import visualisation as pygame_visualisation
from xyworld.display.CursesDisplay import CursesDisplay
from xyworld.display.PygameDisplay import PygameDisplay
from synergine.display.TestDisplay import TestDisplay
from traveller.synergy.TravellerSimulation import TravellerSimulation
from traveller.synergy.TravellerCollection import TravellerCollection
from traveller.synergy.TravellerCollectionConfiguration import TravellerCollectionConfiguration
from traveller.display.visualisation import visualisation as traveller_visualisation
from traveller.display.TravellerDisplay import TravellerDisplay
from traveller.core.Context import Context as TravellerContext
from xyzworld.Context import Context as XyzContext

config = {
    'app': {
        'name': 'Synergine',
        'classes': {
          'Context': XyzContext
        }
    },
    'engine': {
        'fpsmax': 25,
        'debug': {
            'mainprocess': False,
            'cycles': 100
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

config_traveller = {
    'app': {
        'name': 'Traveller',
        'classes': {
            'Context': TravellerContext
        }
    },
    'engine': {
        'fpsmax': 255,
        'debug': {
            'mainprocess': True,
            'cycles': -1
        }
    },
    'simulations' : [TravellerSimulation([TravellerCollection(TravellerCollectionConfiguration())])],
    'connections': [TravellerDisplay],
    'terminal': {
        'pygame': {
            'visualisation': traveller_visualisation,
            'window_size': (800, 600),
            'app': {
                'name': 'Synergine (pygame)'
            },
            'font': {
                'name': 'arial',
                'size': 13
            },
            'display': {
                'grid': {
                    'size': 20
                }
            }
        }
    }
}