from synergine.synergy.object.SynergyObject import SynergyObject as BaseSynergyObject
from xyzworld.cst import POSITION, POSITIONS
from synergine.metas import metas


class SynergyObject(BaseSynergyObject):

    def __init__(self):
        super().__init__()
        self._position = None

    def set_position(self, point):
        if self._position:
          metas.list.remove(POSITIONS, self._position, self.get_id())
        self._position = point
        metas.value.set(POSITION, self.get_id(), point)
        metas.list.add(POSITIONS, point, self.get_id())

    def get_position(self):
        """
        :return: (z, x, y)
        """
        return self._position