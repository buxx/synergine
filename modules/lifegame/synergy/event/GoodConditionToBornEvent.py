from lifegame.synergy.event.AliveAroundEvent import AliveAroundEvent
from synergine.core.exceptions import NotConcernedEvent
from xyzworld.mechanism.AroundMechanism import AroundMechanism
from lifegame.cst import ALIVE, COL_DIED


class GoodConditionToBornEvent(AliveAroundEvent):
    """
    This event is applied when born condition are here. So when exactly 3 alive cell are around of observed cell.
    """

    _mechanism = AroundMechanism
    """This event need to know what is around concerned cell. So we use AroundMechanism who give us list of around
    objects ids."""

    _concern = COL_DIED
    """This event only concern died cells."""

    def _prepare(self, object_id, context, parameters={}):
        """
        According to “Conway’s Game of Life”, event match if exactly 3 around cell are alive.
        """
        cell_near_count = self._get_alive_cell_around_count(context, parameters)
        if cell_near_count is 3:
            return parameters
        #  If event not match, we must raise an NotConcernedEvent.
        raise NotConcernedEvent()
