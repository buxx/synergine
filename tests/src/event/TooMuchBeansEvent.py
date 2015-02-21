from tests.src.event.TestEvent import TestEvent
from tests.src.TestSynergyObject import TestSynergyObject
from tests.src.cst import BEANS


class TooMuchBeansEvent(TestEvent):

    def _object_match(self, object_id, context, parameters={}):
        return context.metas.value.get(BEANS, object_id) > 10000000
