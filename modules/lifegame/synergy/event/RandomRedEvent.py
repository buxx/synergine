import random
from synergine.core.exceptions import NotConcernedEvent
from synergine.synergy.event.Event import Event
from lifegame.cst import COL_ALL


class RandomRedEvent(Event):
    """
    Illustration of double state usage (concern)
    """

    concern = COL_ALL

    def _prepare(self, obj, context, parameters={}):
        if random.randint(0, 50) == 50:
            return parameters
        raise NotConcernedEvent()