import unittest
from src.core.Core import Core
from src.test.TestTerminal import TestTerminal

class TestSimulation(unittest.TestCase):
  
  def setUp(self):
    self._connection = TestTerminal()
  
  def _getSetUpSimulation(self):
    raise NotImplementedError
  
  def _getCoreConfiguration(self, cycles, main_process = True):
    return {
      'engine': {
        'fpsmax': True,
        'debug': {
          'mainprocess': main_process,
          'cycles': range(cycles)
        }
      },
      'simulations' : [self._getSetUpSimulation()],
      'connections': [self._connection]
    }
  
  def getCore(self, cycles=0, main_process=True):
    core = Core(self._getCoreConfiguration(cycles, main_process))
    have_to_be_runned_by = core.haveToBeRunnedBy()
    if have_to_be_runned_by:
      have_to_be_runned_by.encapsulate_run(core.run)
    return core
  
  def _getSynergyObjectManagerForCycle(self, cycles, main_process=True):
    core = self.getCore(cycles, main_process)
    core.run()
    return self._connection.getSynergyObjectManager()
  