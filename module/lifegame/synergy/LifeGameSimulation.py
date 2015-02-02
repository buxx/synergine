from synergine.synergy.Simulation import Simulation
from module.lifegame.synergy.object.Cell import Cell
from synergine.lib.eint import IncrementedNamedInt


class LifeGameSimulation(Simulation):

    ALIVE = IncrementedNamedInt.get('lgs.alive')
    DIED = IncrementedNamedInt.get('lgs.died')

    def __init__(self, collections):
        super().__init__(collections)