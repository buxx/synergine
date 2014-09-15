import unittest
from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.test.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration as TestCollectionConfiguration
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
        'collections' : (LifeGameCollection(TestCollectionConfiguration()),)
      },
      'connections': [self._connection]
    })
  
  def test_cycles_in_main_process(self):
    self._testCycles(True)
  
  def test_cycles_in_sub_process(self):
    self._testCycles(False)
    
  def _testCycles(self, main_process):
    for cycle in (
      (0, 7, [(0, 20, 20),
        (0, 21, 20),
        (0, 22, 20),
        (0, 22, 21),
        (0, 22, 22),
        (0, 21, 22),
        (0, 20, 22)]),
      (1, 7, [(0, 21, 20),
        (0, 22, 20),
        (0, 22, 22),
        (0, 21, 22),
        (0, 21, 19),
        (0, 21, 23),
        (0, 23, 21)]),
      (2, 9, [(0, 21, 20),
        (0, 22, 20),
        (0, 22, 22),
        (0, 21, 22),
        (0, 21, 19),
        (0, 21, 23),
        (0, 23, 21),
        (0, 22, 19),
        (0, 22, 23)]),
      (3, 9, [(0, 21, 20),
        (0, 21, 22),
        (0, 21, 19),
        (0, 21, 23),
        (0, 23, 21),
        (0, 22, 19),
        (0, 22, 23),
        (0, 23, 20),
        (0, 23, 22)]),
      (4, 10, [(0, 21, 20),
        (0, 21, 22),
        (0, 21, 19),
        (0, 21, 23),
        (0, 23, 21),
        (0, 22, 19),
        (0, 22, 23),
        (0, 23, 20),
        (0, 23, 22),
        (0, 24, 21)]),
      (5, 12, [(0, 21, 20),
        (0, 21, 22),
        (0, 21, 19),
        (0, 21, 23),
        (0, 23, 21),
        (0, 22, 19),
        (0, 22, 23),
        (0, 23, 20),
        (0, 23, 22),
        (0, 24, 21),
        (0, 24, 20),
        (0, 24, 22)]),
      (10, 20, [(0, 21, 19),
        (0, 21, 23),
        (0, 20, 19),
        (0, 20, 23),
        (0, 22, 17),
        (0, 22, 25),
        (0, 26, 21),
        (0, 20, 18),
        (0, 20, 24),
        (0, 21, 17),
        (0, 21, 25),
        (0, 23, 17),
        (0, 23, 21),
        (0, 23, 25),
        (0, 24, 18),
        (0, 24, 24),
        (0, 25, 19),
        (0, 25, 23),
        (0, 26, 20),
        (0, 26, 22)])
    ):
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