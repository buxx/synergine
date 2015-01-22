from synergine.src.synergy.Simulation import Simulation
from module.lifegame.synergy.object.Cell import Cell
from synergine.lib.eint import IncrementedNamedInt


class LifeGameSimulation(Simulation):

    ALIVE = IncrementedNamedInt.get('lgs.alive')
    DIED = IncrementedNamedInt.get('lgs.died')
    POSITION = IncrementedNamedInt.get('lgs.position')
    POSITIONS = IncrementedNamedInt.get('lgs.positions')

    def __init__(self, collections):
        super().__init__(collections)