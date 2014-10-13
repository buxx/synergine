from synergine.src.synergy.event.Action import Action
from tests.src.event.MakeBeansProfitEvent import MakeBeansProfitEvent

class MakeBeansProfitAction(Action):

    _listen = MakeBeansProfitEvent

    def run(self, collection, context):
        self._obj.beans = self._obj.beans ** self._obj.coeff

