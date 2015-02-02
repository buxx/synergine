import unittest
from synergine.test.TestSimulation import TestSimulation as BaseTestSimulation
from module.lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from module.lifegame.test.src.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration as TestCollectionConfiguration
from module.lifegame.test.src.test_context import test_context
from module.xyzworld.Context import Context as XyzContext


class TestLifeGameSimulation(BaseTestSimulation):

    def _get_set_up_simulation(self):
        return LifeGameSimulation([LifeGameCollection(TestCollectionConfiguration())])

    def _get_core_configuration(self, cycles, main_process = True):
      config = super()._get_core_configuration(cycles, main_process)
      config.update({
        'app': {
          'classes': {
            'Context': XyzContext
          }
        }
      })
      return config

    def test_cycles_in_main_process(self):
        self._test_cycles(True)

    def test_cycles_in_sub_process(self):
        self._test_cycles(False)

    def _test_cycles(self, main_process):
        new_test_context = []
        for cycle in test_context:
            synergy_object_manager = self._get_synergy_object_manager_for_cycle(cycles=cycle[0]+1, main_process=main_process)
            self.assertEqual(cycle[1], len(self._get_alive_cells(synergy_object_manager.get_objects())))

            for point in cycle[2]:
                self.assertTrue(self._cell_exist_in_point(synergy_object_manager, point))

    def _get_alive_cells(self, cells):
        return [cell for cell in cells if cell.is_alive()]

    def _cell_exist_in_point(self, synergy_object_manager, point):
        for obj in self._get_alive_cells(synergy_object_manager.get_objects()):
            obj_point = obj.get_point()
            obj_test_data = (obj_point[0], obj_point[1], obj_point[2], obj.get_is_alive_since()+1)
            # En fait c'est les objets retournes par core qui sont ceux du debut ... la simu a tourne ? debugger
            if obj_test_data == point:
                return True
        return False