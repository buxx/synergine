import unittest

from lifegame.display.curses_visualisation import visualisation
from xyworld.display.object.TextTraceVisualisation import TextTraceVisualisation
from synergine.core.display.ObjectVisualizer import ObjectVisualizer
from lifegame.synergy.object.Cell import Cell
from synergine.core.cycle.Context import Context


class TestVisualisation(unittest.TestCase):

    def setUp(self):
        self._object_visualizer = ObjectVisualizer(visualisation, Context())

    def test_cells_render(self):
        cell = Cell(object(), object())
        cell.set_alive(True)

        self._test_cell_char(cell, -1, 'o')
        for life_cycle in ((0, 'o'), (1, 'O'), (2, '0'), (3, '0')):
            cell.end_cycle()
            self._test_cell_char(cell, life_cycle[0], life_cycle[1])

    def _test_cell_char(self, cell, alive_since, char):
        self.assertEqual(alive_since, cell.get_is_alive_since())
        cell_visual = self._object_visualizer.get_visual(cell)
        self.assertIsInstance(cell_visual, TextTraceVisualisation)
        self.assertEqual(char, cell_visual.get_char())