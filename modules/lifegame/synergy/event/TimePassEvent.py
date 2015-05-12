from synergine.synergy.event.Event import Event
from lifegame.cst import COL_ALL


class TimePassEvent(Event):

    _concern = COL_ALL
    """All cell are concerned"""

    def _prepare(self, obj, context, parameters={}):
        # All cells are concerned
        return parameters
