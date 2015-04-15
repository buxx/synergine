from tests.src.event.TestEvent import TestEvent
from tests.src.TestSynergyObject import TestSynergyObject


class MakeBeansProfitEvent(TestEvent):

    def _prepare(self, object_id, context, parameters={}):
        return parameters