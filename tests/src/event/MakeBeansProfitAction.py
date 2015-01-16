from synergine.src.synergy.event.Action import Action
from tests.src.event.MakeBeansProfitEvent import MakeBeansProfitEvent

class MakeBeansProfitAction(Action):

    _listen = MakeBeansProfitEvent

    def run(self, obj, collection, context):
        obj.beans = obj.beans ** obj.coeff

