from synergine.src.synergy.event.Action import Action
from module.lifegame.synergy.event.NotGoodConditionToPersistEvent import NotGoodConditionToPersistEvent
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from synergine.metas import metas


class DieAction(Action):

    _listen = NotGoodConditionToPersistEvent

    def run(self, obj, collection, context):
        obj.set_alive(False)
        metas.list.add(LifeGameSimulation.STATE, obj.get_id(), LifeGameSimulation.DIED)
        metas.list.remove(LifeGameSimulation.STATE, obj.get_id(), LifeGameSimulation.ALIVE)