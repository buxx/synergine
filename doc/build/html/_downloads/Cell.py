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

    def set_alive(self, alive):
        """
        Some text
        :param alive: Foo
        :return: Void
        """
        #  When alive state of Cell change, self._alive is reinitialized
        self._alive_since = -1
        self._alive = alive

    def is_alive(self):
        return self._alive

    def get_is_alive_since(self):
        return self._alive_since

    def end_cycle(self):
        """
        At each cycle, cell is more older if it's alive.
        :return:
        """
        if self.is_alive():
            self._alive_since += 1
