from synergine.synergy.event.Action import Action
from lifegame.synergy.event.NotGoodConditionToPersistEvent import NotGoodConditionToPersistEvent
from lifegame.cst import DIED, ALIVE
from synergine.metas import metas


class DieAction(Action):

    _listen = NotGoodConditionToPersistEvent

    def run(self, obj, collection, context, synergy_manager):
        obj.set_alive(False)
        metas.states.add(obj.get_id(), DIED)
        metas.states.remove(obj.get_id(), ALIVE)