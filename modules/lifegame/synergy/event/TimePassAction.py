from synergine.synergy.event.Action import Action
from lifegame.synergy.event.TimePassEvent import TimePassEvent
from lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from synergine.metas import metas
from lifegame.synergy.event.DieAction import DieAction
from lifegame.synergy.event.BornAction import BornAction


class TimePassAction(Action):

    _listen = TimePassEvent
    _depend = [BornAction, DieAction]

    def run(self, obj, collection, context):
        obj.end_cycle()
        pass
        pass