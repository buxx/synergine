from synergine.src.synergy.event.Action import Action
from tests.src.event.TooMuchBeansEvent import TooMuchBeansEvent
from tests.src.event.MakeBeansProfitAction import MakeBeansProfitAction

class TooMuchBeansAction(Action):

    _listen = TooMuchBeansEvent
    _depend = [MakeBeansProfitAction]

    def run(self, obj, collection, context):
        obj.beans = 0
