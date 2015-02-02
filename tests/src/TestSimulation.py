from synergine.synergy.Simulation import Simulation
from synergine.lib.eint import IncrementedNamedInt

class TestSimulation(Simulation):

    COMPUTABLE = IncrementedNamedInt.get('t.computable')
    BEANS = IncrementedNamedInt.get('t.beans')

    def __init__(self, collections):
        super().__init__(collections)
