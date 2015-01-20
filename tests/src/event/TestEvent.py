from synergine.src.synergy.event.Event import Event
from tests.src.TestSimulation import TestSimulation


class TestEvent(Event):

    def concern(self, obj, context):
        return context.metas.have_state(obj, TestSimulation.COMPUTABLE)

    def _object_match(self, obj, context, parameters={}):
        return True