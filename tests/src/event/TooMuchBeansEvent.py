from tests.src.event.TestEvent import TestEvent
from tests.src.TestSynergyObject import TestSynergyObject

class TooMuchBeansEvent(TestEvent):

    def _object_match(self, obj, context, parameters={}):
        return obj.beans > 10000000
