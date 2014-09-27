import unittest
from src.test.TestSimulation import TestSimulation as BaseTestSimulation
from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.test.src.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration as TestCollectionConfiguration
from module.lifegame.test.src.test_context import test_context

class TestLifeGameSimulation(BaseTestSimulation):
  
  def _getSetUpCollections(self):
    return [LifeGameCollection(TestCollectionConfiguration())]
  
  def test_cycles_in_main_process(self):
    self._testCycles(True)
  
  def test_cycles_in_sub_process(self):
    self._testCycles(False)
    
  def _testCycles(self, main_process):
    for cycle in test_context:
      synergy_object_manager = self._getSynergyObjectManagerForCycle(cycles=cycle[0]+1, main_process=main_process)
      self.assertEqual(cycle[1], len(synergy_object_manager.getObjects()))
      for point in cycle[2]:
        self.assertTrue(self._cellExistInPoint(synergy_object_manager, point))
      
  #def _getObjectsPositions(self, objects):
  #  positions = []
  #  for obj in objects:
  #    positions.append(obj.getPoint())
  #  return positions
  
  def _cellExistInPoint(self, synergy_object_manager, point):
    for obj in synergy_object_manager.getObjects():
      if obj.getPoint() == point:
        return True
    return False