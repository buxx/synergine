from os import getcwd
from sys import path as ppath
ppath.insert(1,getcwd()+'/modules')

from synergine.core.Core import Core
from config import config


if __name__ == '__main__':
    Core.start_core(config, modules_path='modules')