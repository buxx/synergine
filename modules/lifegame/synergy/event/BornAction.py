from synergine.synergy.event.Action import Action
from lifegame.synergy.event.GoodConditionToBornEvent import GoodConditionToBornEvent
from lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from synergine.metas import metas


class BornAction(Action):

    _listen = GoodConditionToBornEvent

    def run(self, obj, collection, context, synergy_manager):
        obj.set_alive(True)
        metas.list.add(LifeGameSimulation.STATE, obj.get_id(), LifeGameSimulation.ALIVE)
        metas.list.remove(LifeGameSimulation.STATE, obj.get_id(), LifeGameSimulation.DIED)