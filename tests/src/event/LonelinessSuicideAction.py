from synergine.synergy.event.Action import Action
from tests.src.event.LonelinessSuicideEvent import LonelinessSuicideEvent
from tests.src.event.TooMuchBeansAction import TooMuchBeansAction


class LonelinessSuicideAction(Action):

    _listen = LonelinessSuicideEvent
    _depend = [TooMuchBeansAction]

    def run(self, obj, context, synergy_manager):
        obj.get_collection().remove_object(obj)