from synergine.synergy.event.Event import Event
from tests.src.TestSimulation import TestSimulation


class TestEvent(Event):

    def concern(self, object_id, context):
        return context.metas.list.have(TestSimulation.STATE, object_id, TestSimulation.COMPUTABLE)

    def _object_match(self, object_id, context, parameters={}):
        return True