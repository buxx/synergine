from synergine.synergy.event.Action import Action
from lifegame.synergy.event.GoodConditionToBornEvent import GoodConditionToBornEvent
from lifegame.cst import DIED, ALIVE


class BornAction(Action):

    _listen = GoodConditionToBornEvent

    def run(self, obj, collection, context, synergy_manager):
        obj.set_alive(True)
        context.metas.states.add_remove(obj.get_id(), ALIVE, DIED)