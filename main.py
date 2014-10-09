from src.core.Core import Core
from config import config

if __name__ == '__main__':
    core = Core(config)
    have_to_be_runned_by = core.haveToBeRunnedBy()
    if have_to_be_runned_by:
        have_to_be_runned_by.encapsulate_run(core.run)
    else:
        core.run()