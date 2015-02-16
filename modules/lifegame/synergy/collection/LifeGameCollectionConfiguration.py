from synergine.synergy.collection.Configuration import Configuration
from lifegame.synergy.object.Cell import Cell
from synergine.metas import metas
from lifegame.cst import DIED, ALIVE


class LifeGameCollectionConfiguration(Configuration):

    def get_start_objects(self, collection):
        cells = []
        # cell grid
        for x in range(40):
            for y in range(50):
                cell = Cell()
                cell.set_position((0, x, y))
                cells.append(cell)

        alive_cell_traces = (
            (0, 20, 20),
            (0, 21, 20),
            (0, 22, 20),
            (0, 22, 21),
            (0, 22, 22),
            (0, 21, 22),
            (0, 20, 22)
        )
        for dead_cell in cells:
            if dead_cell.get_position() in alive_cell_traces:
                dead_cell.set_alive(True)
                metas.states.add(dead_cell.get_id(), ALIVE)
            else:
                metas.states.add(dead_cell.get_id(), DIED)

        return cells