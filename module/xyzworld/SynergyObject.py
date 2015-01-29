from synergine.src.synergy.object.SynergyObject import SynergyObject as BaseSynergyObject
from module.xyzworld.cst import *


class SynergyObject(BaseSynergyObject):

    def __init__(self):
        # TODO: Cet histoire de trace est trop dependante d'objet a trace
        super().__init__()
        self._trace_length = 1
        self._trace = []

    # TODO: Gestion space dtata autrement ?
    def add_trace(self, point):
        # TODO: limite de taille de
        try:
          previous_point = self.get_point()
          # TODO: constantes (string utilise a cause de double import LifeGameSim)
          metas.list.remove(POSITIONS, previous_point, self.get_id())
        except IndexError:
          pass
        metas.list.add(POSITIONS, point, self.get_id())
        self._trace.append(point)
        metas.value.set(POSITION, self.get_id(), point)

    def get_trace(self):
        return self._trace

    def get_point(self):
        """
        Return the last insered trace point
        :return: (z, x, y)
        """
        trace = self.get_trace()
        return trace[len(trace)-1]