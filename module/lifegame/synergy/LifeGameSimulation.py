from synergine.src.synergy.Simulation import Simulation
from module.lifegame.synergy.object.Cell import Cell

class LifeGameSimulation(Simulation):

    ALIVE = 'alive'
    DIED = 'died'
    # TODO: DIED = IncrementedNamedInt('DIED')

    def __init__(self, collections):
        super().__init__(collections)