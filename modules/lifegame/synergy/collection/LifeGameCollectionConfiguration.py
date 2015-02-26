from synergine.synergy.collection.Configuration import Configuration
from lifegame.synergy.object.Cell import Cell
from lifegame.cst import DIED, ALIVE, COL_ALL, COL_DIED, COL_ALIVE


class LifeGameCollectionConfiguration(Configuration):

    def get_start_objects(self, collection, context):
        cells = []
        # cell grid
        for x in range(40):
            for y in range(50):
                cell = Cell(collection, context)
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
            context.metas.collections.add(dead_cell.get_id(), COL_ALL)
            if dead_cell.get_position() in alive_cell_traces:
                dead_cell.set_alive(True)
                context.metas.states.add(dead_cell.get_id(), ALIVE)
                context.metas.collections.add(dead_cell.get_id(), COL_ALIVE)
            else:
                context.metas.states.add(dead_cell.get_id(), DIED)
                context.metas.collections.add(dead_cell.get_id(), COL_DIED)
        return cells