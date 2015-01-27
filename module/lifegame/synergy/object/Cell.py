from synergine.src.synergy.object.SynergyObject import SynergyObject
from synergine.lib.eint import IncrementedNamedInt
from synergine.metas import metas


class Cell(SynergyObject):

    def __init__(self):
        super().__init__()
        self._alive = False
        self._alive_since = 0
        self._died_since = 0
        self.test = 0

    def add_trace(self, point):
        """
        Cell have only one point length
        """
        if self._trace:
          metas.list.remove(IncrementedNamedInt.get_for_name('lgs.positions'), self.get_point(), self.get_id())
        metas.list.add(IncrementedNamedInt.get_for_name('lgs.positions'), point, self.get_id())
        self._trace.append(point)
        metas.value.set(IncrementedNamedInt.get_for_name('lgs.position'), self.get_id(), point)
        self._trace = [point]

    def set_point(self, point):
        self.add_trace(point)

    def get_point(self):
        return self.get_trace()[0]

    def set_alive(self, alive):
        self._alive_since = -1
        self._died_since = -1
        self._alive = alive

    def is_alive(self):
        return self._alive

    def get_is_alive_since(self):
        return self._alive_since

    def get_is_died_since(self):
        return self._died_since

    def end_cycle(self):
        if self.is_alive():
            self._alive_since += 1
        else:
            self._died_since += 1