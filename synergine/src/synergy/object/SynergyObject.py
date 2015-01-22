from synergine.src.synergy.object.SynergyObjectInterface import SynergyObjectInterface
from synergine.lib.eint import IncrementedNamedInt
from synergine.metas import metas


class SynergyObject(SynergyObjectInterface):

    SIGNAL_CREATED = 'object.created'
    SIGNAL_DELETED = 'object.deleted'

    def __init__(self):
        self._cycle_frequency = 1
        # TODO: Cet histoire de trace est trop dependante d'objet a trace
        self._trace_length = 1
        self._trace = []
        self._id = IncrementedNamedInt.get(self)

    def get_id(self):
        return self._id

    # TODO: Gestion space dtata autrement ?
    def add_trace(self, point):
        # TODO: limite de taille de
        try:
          previous_point = self.get_point()
          # TODO: constantes (string utilise a cause de double import LifeGameSim)
          metas.list.remove(IncrementedNamedInt.get_for_name('lgs.positions'), previous_point, self.get_id())
        except IndexError:
          pass
        metas.list.add(IncrementedNamedInt.get_for_name('lgs.positions'), point, self.get_id())
        self._trace.append(point)
        metas.value.set(IncrementedNamedInt.get_for_name('lgs.position'), self.get_id(), point)

    def get_trace(self):
        return self._trace

    def get_point(self):
        """
        Return the last insered trace point
        :return: (z, x, y)
        """
        trace = self.get_trace()
        return trace[len(trace)-1]

    def end_cycle(self):
        pass