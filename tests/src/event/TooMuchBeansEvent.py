from synergine.core.exceptions import NotConcernedEvent
from tests.src.event.TestEvent import TestEvent
from tests.src.cst import BEANS


class TooMuchBeansEvent(TestEvent):

    def _prepare(self, object_id, context, parameters={}):
        if not context.metas.value.get(BEANS, object_id) > 10000000:
            raise NotConcernedEvent()
        return parameters
