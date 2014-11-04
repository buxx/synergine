from synergine.src.core.Core import Core
from config import config_traveller

if __name__ == '__main__':
    Core.start_core(config_traveller, modules_path='module')