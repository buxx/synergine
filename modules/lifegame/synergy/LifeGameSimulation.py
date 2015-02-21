from synergine.synergy.Simulation import Simulation
from lifegame.synergy.object.Cell import Cell
from synergine.lib.eint import IncrementedNamedInt
from lifegame.cst import ALIVE, DIED, COL_ALL, COL_DIED, COL_ALIVE
from lifegame.synergy.event.BornAction import BornAction
from lifegame.synergy.event.DieAction import DieAction


class LifeGameSimulation(Simulation):

    def __init__(self, collections):
        super().__init__(collections)

    def connect_actions_signals(self, Signals):
        Signals.signal(BornAction).connect(lambda obj, context: \
            context.metas.collections.add_remove(obj.get_id(), COL_ALIVE, COL_DIED))
        Signals.signal(DieAction).connect(lambda obj, context: \
            context.metas.collections.add_remove(obj.get_id(), COL_DIED, COL_ALIVE))

