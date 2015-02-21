from synergine.synergy.event.Action import Action
from tests.src.event.MakeBeansProfitEvent import MakeBeansProfitEvent
from tests.src.cst import BEANS

class MakeBeansProfitAction(Action):

    _listen = MakeBeansProfitEvent

    def run(self, obj, collection, context, synergy_manager):
        obj.beans = obj.beans ** obj.coeff
        context.metas.value.set(BEANS, obj.get_id(), obj.beans)

