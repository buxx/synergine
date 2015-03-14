from synergine.synergy.object.SynergyObject import SynergyObject as BaseSynergyObject
from xyzworld.cst import POSITION, POSITIONS


class SynergyObject(BaseSynergyObject):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        self._position = None
        self._start_position = None

    def set_position(self, point):
        if self._position:
            self._context.metas.list.remove(POSITIONS, self._position, self.get_id())
        else:
            self._start_position = point
        self._position = point
        self._context.metas.value.set(POSITION, self.get_id(), point)
        self._context.metas.list.add(POSITIONS, point, self.get_id())

    def get_position(self):
        """
        :return: (z, x, y)
        """
        return self._position