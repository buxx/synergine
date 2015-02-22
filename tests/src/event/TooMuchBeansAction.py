from synergine.synergy.event.Action import Action
from tests.src.event.TooMuchBeansEvent import TooMuchBeansEvent
from tests.src.event.MakeBeansProfitAction import MakeBeansProfitAction
from tests.src.cst import BEANS

class TooMuchBeansAction(Action):

    _listen = TooMuchBeansEvent
    _depend = [MakeBeansProfitAction]

    def run(self, obj, collection, context, synergy_manager):
        obj.beans = 0
        context.metas.value.set(BEANS, obj.get_id(), 0)