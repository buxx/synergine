from synergine.synergy.event.Action import Action
from lifegame.synergy.event.NotGoodConditionToPersistEvent import NotGoodConditionToPersistEvent
from lifegame.cst import DIED, ALIVE


class DieAction(Action):

    _listen = NotGoodConditionToPersistEvent

    def run(self, obj, collection, context, synergy_manager):
        obj.set_alive(False)
        context.metas.states.add_remove(obj.get_id(), DIED, ALIVE)