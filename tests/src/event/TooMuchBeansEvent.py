from tests.src.event.TestEvent import TestEvent
from tests.src.TestSynergyObject import TestSynergyObject
from synergine.metas import metas
from tests.src.TestSimulation import TestSimulation


class TooMuchBeansEvent(TestEvent):

    def _object_match(self, object_id, context, parameters={}):
        return metas.value.get(TestSimulation.BEANS, object_id) > 10000000
