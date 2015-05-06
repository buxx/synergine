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
    'connections': [PrintTerminal]
}

if __name__ == '__main__':
    # Run simulation
    Core.start_core(config, modules_path='modules')