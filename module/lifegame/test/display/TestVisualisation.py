import unittest
from module.lifegame.display.curses_visualisation import visualisation
from synergine.src.core.display.ObjectVisualizer import ObjectVisualizer
from module.lifegame.synergy.object.Cell import Cell
from synergine.src.display.object.TextTraceVisualisation import TextTraceVisualisation


class TestVisualisation(unittest.TestCase):

    def setUp(self):
        self._object_visualizer = ObjectVisualizer(visualisation)

    def test_cells_render(self):
        cell = Cell()
        cell.set_alive(True)

        self._test_cell_char(cell, 0, '*')
        for life_cycle in ((1, 'o'), (2, 'O'), (3, '0'), (4, '0')):
            cell.end_cycle()
            self._test_cell_char(cell, life_cycle[0], life_cycle[1])

    def _test_cell_char(self, cell, alive_since, char):
        self.assertEqual(alive_since, cell.get_is_alive_since())
        cell_visual = self._object_visualizer.get_visual(cell)
        self.assertIsInstance(cell_visual, TextTraceVisualisation)
        self.assertEqual(char, cell_visual.get_char())