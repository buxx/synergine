import unittest
from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from src.core.Core import Core
from src.core.connection.Terminal import Terminal

# TODO: Objet generique de testTerminal ?
class TestTerminal(Terminal):
  
  def __init__(self):
    self._synergy_object_manager = None
  
  def receive(self, synergy_object_manager):
    self._synergy_object_manager = synergy_object_manager
  
  def getSynergyObjectManager(self):
    return self._synergy_object_manager

class TestLifeGameSimulation(unittest.TestCase):
  # TODO: Faire un heritage de class pour faciliter le testing
  
  def setUp(self):
    self._connection = TestTerminal()
    # TODO: Configuration ici de Cell par defaut sur LifeGameCollection
    
  # TODO: remonter plus haut
  def getCore(self, cycles, main_process = True):
    return Core({
      'engine': {
        'fpsmax': True,
        'debug': {
          'mainprocess': main_process,
          'cycles': range(cycles)
        }
      },
      'simulation' : {
        'collections' : (LifeGameCollection,)
      },
      'connections': [self._connection]
    })
  
  def test_cycles_in_main_process(self):
    self._testCycles(True)
  
  def test_cycles_in_sub_process(self):
    self._testCycles(False)
    
  def _testCycles(self, main_process):
    for cycle_count in (
      (0, 7),
      (1, 7),
      (2, 9),
      (3, 9),
      (4, 10),
      (5, 12),
      (10, 20),
      (50, 101),
      (100, 103),
    ):
      self.assertEqual(cycle_count[1], len(self._getSynergyObjectManagerForCycle(cycles=cycle_count[0], main_process=main_process).getObjects()))
  
  def _getSynergyObjectManagerForCycle(self, cycles, main_process=True):
    core = self.getCore(cycles, main_process=True)
    core.run()
    return self._connection.getSynergyObjectManager()