from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from module.lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
from module.lifegame.display.curses_visualisation import visualisation as curses_visualisation
from module.lifegame.display.pygame_visualisation import visualisation as pygame_visualisation
from module.xyworld.display.CursesDisplay import CursesDisplay
from module.xyworld.display.PygameDisplay import PygameDisplay
from synergine.src.display.TestDisplay import TestDisplay
from module.traveller.synergy.TravellerSimulation import TravellerSimulation
from module.traveller.synergy.TravellerCollection import TravellerCollection
from module.traveller.synergy.TravellerCollectionConfiguration import TravellerCollectionConfiguration
from module.traveller.display.visualisation import visualisation as traveller_visualisation
from module.traveller.display.TravellerDisplay import TravellerDisplay
from module.traveller.core.Context import Context as TravellerContext
from module.xyzworld.Context import Context as XyzContext

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
            'cycles': range(9999999)
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