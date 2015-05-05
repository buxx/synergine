from synergine.synergy.object.SynergyObject import SynergyObject as BaseSynergyObject
from xyzworld.cst import POSITION, POSITIONS, PREVIOUS_DIRECTION, BLOCKED_SINCE


class SynergyObject(BaseSynergyObject):
    """
    This SynergyObject is designed to support a tri-dimensional environment.
    """

    def __init__(self, collection, context):
        super().__init__(collection, context)
        self._position = None
        self._start_position = None
        self._previous_direction = None

    def set_position(self, point):
        """

        Update the position. Metas are updated to.

        :param point: position of the object, with (z, x, y) signature
        :type point: tuple
        :return:
        """

        #  If a position already exist, we can remove it from metas
        if self._position:
            self._context.metas.list.remove(POSITIONS, self._position, self.get_id())
        else:
            self._start_position = point

        #  If position is different from previous, object has moved.
        if point != self._position:
            self._context.metas.value.set(BLOCKED_SINCE, self.get_id(), 0)

        self._position = point
        self._context.metas.value.set(POSITION, self.get_id(), point)
        self._context.metas.list.add(POSITIONS, point, self.get_id())

    def get_position(self):
        """

        Return the actual position.

        :return: position with (z, x, y) signature
        :rtype: tuple
        """
        return self._position

    def set_previous_direction(self, previous_direction):
        """

        Update the previous position of object.
        TODO: Directions pythons files must be move in xyz module.

        :param previous_direction: The previous direction
        :return:
        """
        self._previous_direction = previous_direction
        self._context.metas.value.set(PREVIOUS_DIRECTION, self.get_id(), previous_direction)

    def get_previous_direction(self):
        """

        Return the previous direction of object

        :return: The previous direction
        :rtype: int
        """
        return self._previous_direction