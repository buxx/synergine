from synergine.synergy.event.Action import Action
from tests.src.event.TooMuchBeansEvent import TooMuchBeansEvent
from tests.src.event.MakeBeansProfitAction import MakeBeansProfitAction
from synergine.metas import metas
from tests.src.TestSimulation import TestSimulation

class TooMuchBeansAction(Action):

    _listen = TooMuchBeansEvent
    _depend = [MakeBeansProfitAction]

    def run(self, obj, collection, context, synergy_manager):
        obj.beans = 0
        metas.value.set(TestSimulation.BEANS, obj.get_id(), 0)