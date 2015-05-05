from synergine.synergy.Simulation import Simulation
from lifegame.cst import COL_DIED, COL_ALIVE
from lifegame.synergy.event.BornAction import BornAction
from lifegame.synergy.event.DieAction import DieAction


class LifeGameSimulation(Simulation):

    def connect_actions_signals(self, signals):
        signals.signal(BornAction).connect(
            lambda obj, context: context.metas.collections.add_remove(obj.get_id(), COL_ALIVE, COL_DIED))
        signals.signal(DieAction).connect(
            lambda obj, context: context.metas.collections.add_remove(obj.get_id(), COL_DIED, COL_ALIVE))
