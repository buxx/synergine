from synergine.src.synergy.event.Action import Action
from module.lifegame.synergy.event.NotGoodConditionToPersistEvent import NotGoodConditionToPersistEvent

class DieAction(Action):

    _listen = NotGoodConditionToPersistEvent

    def run(self, collection, context):
        self._obj.set_alive(False)