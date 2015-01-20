from synergine.src.synergy.event.Action import Action
from module.lifegame.synergy.event.NotGoodConditionToPersistEvent import NotGoodConditionToPersistEvent
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from synergine.src.core.Core import Core


class DieAction(Action):

    _listen = NotGoodConditionToPersistEvent

    def run(self, obj, collection, context):
        obj.set_alive(False)
        Core.metas.set(obj, LifeGameSimulation.DIED)
        Core.metas.unset(obj, LifeGameSimulation.ALIVE)