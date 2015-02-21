from synergine.synergy.event.Event import Event
from tests.src.cst import COL_COMPUTABLE


class TestEvent(Event):

    concern = COL_COMPUTABLE

    def _object_match(self, object_id, context, parameters={}):
        return True