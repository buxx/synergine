from lifegame.cst import COL_ALL, DIED, ALIVE, COL_DIED, COL_ALIVE
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
        context.metas.collections.add(self.get_id(), COL_ALL)
        context.metas.collections.add(self.get_id(), COL_DIED)
        context.metas.states.add(self.get_id(), DIED)  # By default, a cell is dead

    def set_alive(self, alive):
        """

        Change the state of Cell.

        :param alive: Foo
        :return: Void
        """

        #  When alive state of Cell change, self._alive is reinitialized
        self._alive_since = -1
        self._alive = alive

        # We update states to.
        if alive:
            # State of cell is now ALIVE
            self._context.metas.states.add_remove(self.get_id(), ALIVE, DIED)
            # Cell is now in COL_ALIVE collection
            self._context.metas.collections.add(self.get_id(), COL_ALIVE)
            self._context.metas.collections.remove(self.get_id(), COL_DIED)
        else:
            # State of cell is now DIED
            self._context.metas.states.add_remove(self.get_id(), DIED, ALIVE)
            # Cell is now in COL_DIED collection
            self._context.metas.collections.add(self.get_id(), COL_DIED)
            self._context.metas.collections.remove(self.get_id(), COL_ALIVE)

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
