from src.core.Core import Core

if __name__ == '__main__':
  core = Core()
  have_to_be_runned_by = core.haveToBeRunnedBy()
  if have_to_be_runned_by:
    have_to_be_runned_by.encapsulate_run(core.run)
  else:
    core.run()