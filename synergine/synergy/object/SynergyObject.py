from synergine.cst import COL_ALL
from synergine.synergy.object.SynergyObjectInterface import SynergyObjectInterface
from synergine.lib.eint import IncrementedNamedInt


class SynergyObject(SynergyObjectInterface):
    """
    :ivar _collection: Foo
    :ivar _cycle_frequency: Bar
    """

    def __init__(self, collection, context):
        self._collection = collection
        self._cycle_frequency = 1
        self._id = IncrementedNamedInt.get(self)
        self._context = context
        self._add_col(COL_ALL)

    def _add_state(self, state, **kwargs):
        """

        Shortcut to  self._context.metas.states.add

        :param state: State
        :return:
        """
        self._context.metas.states.add(self.get_id(), state, **kwargs)

    def _remove_state(self, state, **kwargs):
        """

        Shortcut to  self._context.metas.states.remove

        :param state: State
        :return:
        """
        self._context.metas.states.remove(self.get_id(), state, **kwargs)

    def _add_col(self, col, **kwargs):
        """

        Shortcut to  self._context.metas.collections.add

        :param col: COL
        :return:
        """
        self._context.metas.collections.add(self.get_id(), col, **kwargs)

    def _remove_col(self, col, **kwargs):
        """

        Shortcut to  self._context.metas.collections.remove

        :param col: COL
        :return:
        """
        self._context.metas.collections.remove(self.get_id(), col, **kwargs)

    def get_collection(self):
        """

        Return the Collection who contain this

        :return: The Collection who contain this
        :rtype: SynergyCollection
        """
        return self._collection

    def get_id(self):
        """

        Return the unique id of this object

        :return: Unique id of this object
        :rtype: int
        """
        return self._id

    def initialize(self):
        """

        You can place code here to initialize object after his creation and before simulation start.

        :return:
        """
        pass
