from synergine.core.cycle.Context import Context as BaseContext


class Context(BaseContext):

    def __init__(self, synergy_object_manager):
        super().__init__(synergy_object_manager)
        self._pheromon_traces = {}

    def add_pheromon_trace(self, towns, intensity):
        previous_town = None
        for town in towns:
            if previous_town:
                couple = (previous_town, town)
                iverted_couple = (town, previous_town)
                if couple in self._pheromon_traces:
                    self._pheromon_traces[couple] += intensity
                    self._pheromon_traces[iverted_couple] += intensity
                else:
                    self._pheromon_traces[couple] = intensity
                    self._pheromon_traces[iverted_couple] = intensity
            previous_town = town

    def get_road_intensity(self, town_a, town_b):
        couple = (town_a, town_b)
        if couple in self._pheromon_traces:
            return self._pheromon_traces[couple]
        return 1

    def reduce_pheromons_intensitys(self):
        for couple in self._pheromon_traces:
            self._pheromon_traces[couple] -= 1
            if self._pheromon_traces[couple] < 0:
                self._pheromon_traces[couple] = 0