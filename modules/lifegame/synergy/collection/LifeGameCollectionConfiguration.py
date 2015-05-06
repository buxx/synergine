from synergine.synergy.collection.Configuration import Configuration
from lifegame.synergy.object.Cell import Cell


class LifeGameCollectionConfiguration(Configuration):

    def get_start_objects(self, collection, context):
        cells = []

        # We build a grid of 40x50 cells
        for x in range(40):
            for y in range(50):
                cell = Cell(collection, context)
                cell.set_position((0, x, y))
                cells.append(cell)

        # We define some position for alive cells
        alive_cell_positions = (
            (0, 20, 20),
            (0, 21, 20),
            (0, 22, 20),
            (0, 22, 21),
            (0, 22, 22),
            (0, 21, 22),
            (0, 20, 22)
        )

        # And we born these alive cell
        for dead_cell in cells:
            if dead_cell.get_position() in alive_cell_positions:
                dead_cell.set_alive(True)

        # Synergy objects can be return to the collection
        return cells