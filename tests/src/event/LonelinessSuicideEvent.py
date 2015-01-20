from tests.src.event.TestEvent import TestEvent
from tests.src.TestSynergyObject import TestSynergyObject


class LonelinessSuicideEvent(TestEvent):

    def __init__(self, actions):
        super().__init__(actions)
        self._concerneds = [TestSynergyObject]

    def _object_match(self, obj, context, parameters={}):
        return not self._has_friends_with_beans(obj, context)

    def _has_friends_with_beans(self, obj, context):
        friends_with_beans_count = 0
        # TODO: .get_collections: Pas adapte si d'autres collections dans la simu !
        for collection in context.get_collections():
            for friend in collection.get_objects():
                if friend.beans > 1:
                    friends_with_beans_count += 1
        if friends_with_beans_count == 0:
            return False
        return True
