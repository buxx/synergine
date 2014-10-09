import unittest
from src.test.TestSimulation import TestSimulation as BaseTestSimulation
from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from module.lifegame.test.src.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration as TestCollectionConfiguration
from module.lifegame.test.src.test_context import test_context

class TestLifeGameSimulation(BaseTestSimulation):

    def _get_set_up_simulation(self):
        return LifeGameSimulation([LifeGameCollection(TestCollectionConfiguration())])

    def test_cycles_in_main_process(self):
        self._test_cycles(True)

    def test_cycles_in_sub_process(self):
        self._test_cycles(False)

    def _test_cycles(self, main_process):
        for cycle in test_context:
            synergy_object_manager = self._get_synergy_object_managerForCycle(cycles=cycle[0]+1, main_process=main_process)
            self.assertEqual(cycle[1], len(self._get_alive_cells(synergy_object_manager.get_objects())))
            for point in cycle[2]:
                self.assertTrue(self._cell_exist_in_point(synergy_object_manager, point))

    def _get_alive_cells(self, cells):
        alive_cells = []
        for cell in cells:
            if cell.is_alive():
                alive_cells.append(cell)
        return alive_cells

    def _cell_exist_in_point(self, synergy_object_manager, point):
        for obj in self._get_alive_cells(synergy_object_manager.get_objects()):
            if obj.get_point() == point:
                return True
        return False