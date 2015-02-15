from synergine.synergy.event.Action import Action
from tests.src.event.MakeBeansProfitEvent import MakeBeansProfitEvent
from synergine.metas import metas
from tests.src.TestSimulation import TestSimulation

class MakeBeansProfitAction(Action):

    _listen = MakeBeansProfitEvent

    def run(self, obj, collection, context, synergy_manager):
        obj.beans = obj.beans ** obj.coeff
        metas.value.set(TestSimulation.BEANS, obj.get_id(), obj.beans)

