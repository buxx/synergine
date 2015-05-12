from synergine.synergy.event.Event import Event
from tests.src.cst import COL_COMPUTABLE


class TestEvent(Event):

    _concern = COL_COMPUTABLE

    def _prepare(self, object_id, context, parameters={}):
        return parameters