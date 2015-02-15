#from synergine.core.Core import Core
# TODO: La notion de position appartient a LifeGame (ou a un addon)
from lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from synergine.metas import metas


class Context():
    """
    This object contain a representation of simulation. It's
    used by Action to know what exist in the synergy simulation
    """

    def __init__(self):
        #self._synergy_object_manager = synergy_object_manager
        #self._map = {}
        self.metas = metas
        self._cycle = 0

    def set_cycle(self, cycle):
        self._cycle = cycle

    def get_cycle(self):
      return self._cycle