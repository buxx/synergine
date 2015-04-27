from synergine.core.simulation.MetaDatas import MetaDatas


class Context():
    """
    This object contain a representation of simulation. It's
    used by Action to know what exist in the synergy simulation
    """

    def __init__(self):
        # self._synergy_object_manager = synergy_object_manager
        # self._map = {}
        self.metas = MetaDatas()
        self._cycle = 0
        self._total_chunk = 0
        self._current_chunk_position = 0

    def set_cycle(self, cycle):
        self._cycle = cycle

    def get_cycle(self):
        return self._cycle

    def set_total_chunk(self, total_chunk):
        self._total_chunk = total_chunk

    def get_total_chunk(self):
        return self._total_chunk

    def set_current_chunk_position(self, current_chunk_position):
        self._current_chunk_position = current_chunk_position

    def get_current_chunk_position(self):
        return self._current_chunk_position
