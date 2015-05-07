from os import getcwd
from sys import path as ppath
from synergine.core.Core import Core

# For now we update the python path. It will change in future version.
ppath.insert(1, getcwd()+'/modules')

from lifegame.PrintTerminal import PrintTerminal
from lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
from xyzworld.Context import Context as XyzContext
from xyworld.display.PygameDisplay import PygameDisplay
from lifegame.PlotTerminal import PlotTerminal
from lifegame.display.pygame_visualisation import visualisation as pygame_visualisation

config = {
    'app': {
        'name': 'LifeGame simulation',
        'classes': {
            'Context': XyzContext
        }
    },
    'engine': {
        'fpsmax': 5,
    },
    'simulations': [LifeGameSimulation([LifeGameCollection(LifeGameCollectionConfiguration())])],
    'connections': [PrintTerminal, PygameDisplay, PlotTerminal],
    'terminal': {
        'pygame': {
            'visualisation': pygame_visualisation,
            'window_size': (700, 500),
            'display': {
                'grid': {
                    'size': 20
                }
            }
        },
    }
}

if __name__ == '__main__':
    # Run simulation
    Core.start_core(config, modules_path='modules')