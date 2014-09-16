import unittest
from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.test.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration as TestCollectionConfiguration
from src.core.Core import Core
from src.core.connection.Terminal import Terminal
from module.lifegame.test.simulation.test_context import test_context

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
        'collections' : (LifeGameCollection(TestCollectionConfiguration()),)
      },
      'connections': [self._connection]
    })
  
  def test_cycles_in_main_process(self):
    self._testCycles(True)
  
  def test_cycles_in_sub_process(self):
    self._testCycles(False)
    
  def _testCycles(self, main_process):
    for cycle in test_context:
      synergy_object_manager = self._getSynergyObjectManagerForCycle(cycles=cycle[0], main_process=main_process)
      self.assertEqual(cycle[1], len(synergy_object_manager.getObjects()))
      self.assertEqual(cycle[2], self._getObjectsPositions(synergy_object_manager.getObjects()))
  
  def _getSynergyObjectManagerForCycle(self, cycles, main_process=True):
    core = self.getCore(cycles, main_process=True)
    core.run()
    return self._connection.getSynergyObjectManager()
  
  def _getObjectsPositions(self, objects):
    positions = []
    for obj in objects:
      positions.append(obj.getPoint())
    return positions