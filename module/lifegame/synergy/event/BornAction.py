from synergine.src.synergy.event.Action import Action
from module.lifegame.synergy.event.GoodConditionToBornEvent import GoodConditionToBornEvent
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from synergine.src.core.Core import Core


class BornAction(Action):

    _listen = GoodConditionToBornEvent

    def run(self, obj, collection, context):
        obj.set_alive(True)
        Core.metas.set(obj, LifeGameSimulation.ALIVE)
        Core.metas.unset(obj, LifeGameSimulation.DIED)