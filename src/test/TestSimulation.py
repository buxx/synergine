import unittest
from src.core.Core import Core
from src.test.TestTerminal import TestTerminal

class TestSimulation(unittest.TestCase):
  
  def setUp(self):
    self._connection = TestTerminal()
  
  def _getSetUpCollections(self):
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
      'simulation' : {
        'collections' : self._getSetUpCollections()
      },
      'connections': [self._connection]
    }
  
  def getCore(self, cycles, main_process = True):
    return Core(self._getCoreConfiguration(cycles, main_process))
  
  def _getSynergyObjectManagerForCycle(self, cycles, main_process=True):
    core = self.getCore(cycles, main_process)
    core.run()
    return self._connection.getSynergyObjectManager()
  