from synergine.src.synergy.collection.Configuration import Configuration
from module.lifegame.synergy.object.Cell import Cell
from synergine.src.core.Core import Core
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation


class LifeGameCollectionConfiguration(Configuration):

    def get_start_objects(self):
        cells = []
        # cell grid
        for x in range(40):
            for y in range(50):
                cell = Cell()
                cell.add_trace((0, x, y))
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
            if dead_cell.get_point() in alive_cell_traces:
                dead_cell.set_alive(True)
                Core.metas.set(dead_cell, LifeGameSimulation.ALIVE)
            else:
                Core.metas.set(dead_cell, LifeGameSimulation.DIED)

        return cells