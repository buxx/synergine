from synergine.synergy.event.Action import Action
from lifegame.synergy.event.GoodConditionToBornEvent import GoodConditionToBornEvent
from lifegame.cst import DIED, ALIVE
from synergine.metas import metas


class BornAction(Action):

    _listen = GoodConditionToBornEvent

    def run(self, obj, collection, context, synergy_manager):
        obj.set_alive(True)
        metas.states.add(obj.get_id(), ALIVE)
        metas.states.remove(obj.get_id(), DIED)