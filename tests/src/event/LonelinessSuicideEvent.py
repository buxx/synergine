from synergine.core.exceptions import NotConcernedEvent
from tests.src.event.TestEvent import TestEvent
from tests.src.cst import BEANS, COMPUTABLE
from tests.src.TestSimulation import TestSimulation


class LonelinessSuicideEvent(TestEvent):

    def __init__(self, actions):
        super().__init__(actions)

    def _prepare(self, object_id, context, parameters={}):
        if self._has_friends_with_beans(context):
            raise NotConcernedEvent()
        return parameters

    @staticmethod
    def _has_friends_with_beans(context):
        friends_with_beans_count = 0
        for friend_id in context.metas.list.get(TestSimulation.STATE, COMPUTABLE):
            friend_beans = context.metas.value.get(BEANS, friend_id)
            if friend_beans > 1:
                friends_with_beans_count += 1
        if friends_with_beans_count == 0:
            return False
        return True
