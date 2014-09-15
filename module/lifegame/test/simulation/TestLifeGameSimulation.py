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
    
  # TODO: remonter plus haut
  def getCore(self, cycles, main_process = True):
    return Core({
      'engine': {
        'fpsmax': 99999, # TODO: Valeur infini ? True
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
    core = self.getCore(cycles=1, main_process=True)
    core.run()
    synergy_object_manager = self._connection.getSynergyObjectManager()
    self.assertEqual(7, len(synergy_object_manager.getObjects()))