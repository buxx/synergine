from synergine.src.synergy.event.Action import Action
from tests.src.event.LonelinessSuicideEvent import LonelinessSuicideEvent
from tests.src.event.TooMuchBeansAction import TooMuchBeansAction

class LonelinessSuicideAction(Action):

    _listen = LonelinessSuicideEvent
    _depend = [TooMuchBeansAction]

    def run(self, obj, collection, context):
        collection.remove_object(obj)
