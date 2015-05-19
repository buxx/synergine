from synergine.cst import COL_ALL
from lifegame.cst import DIED, ALIVE, COL_DIED, COL_ALIVE
from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject


class Cell(XyzSynergyObject):
    """
    Representation of cell.
    """

    def __init__(self, collection, context):
        """

        :param collection: Collection who contain this Cell
        :param context: The context object
        """
        super().__init__(collection, context)
        self._alive = False
        self._alive_since = -1
        # By default, a cell is dead
        self._add_col(COL_DIED)
        self._add_state(DIED)

    def set_alive(self, alive):
        """

        Change the state of Cell.

        :param alive: Alive boolean
        :return:
        """

        #  When alive state of Cell change, self._alive is reinitialized
        self._alive_since = -1
        self._alive = alive

        # We update states to.
        if alive:
            # State of cell is now ALIVE
            self._add_state(ALIVE)
            self._remove_state(DIED)
            # Cell is now in COL_ALIVE collection
            self._add_col(COL_ALIVE)
            self._remove_col(COL_DIED)
        else:
            # State of cell is now DIED
            self._add_state(DIED)
            self._remove_state(ALIVE)
            # Cell is now in COL_DIED collection
            self._add_col(COL_DIED)
            self._remove_col(COL_ALIVE)

    def is_alive(self):
        return self._alive

    def get_is_alive_since(self):
        """

        :return: Count of alive cycles.
        :rtype: int
        """
        return self._alive_since

    def end_cycle(self):
        """

        At each cycle, cell is more older if it's alive.

        :return:
        """
        if self.is_alive():
            self._alive_since += 1
