from synergine.synergy.object.SynergyObject import SynergyObject


class Traveller(SynergyObject):

    def __init__(self):
        super().__init__()
        self._start_town = None
        self._town = None
        self._towns = []
        self._distance = 0
        self._previous_distance = 0
        self._last_pheromon_intensity = 1

    def _set_town(self, town):
        self._town = town

    def get_town(self):
        return self._town

    def add_town(self, town, distance=0):
        if not len(self._towns):
            self._start_town = town
        self._towns.append(town)
        self._set_town(town)
        self.set_position(town.get_position())
        self._distance += distance

    def get_towns(self):
        return self._towns

    def reinit_travel(self):
        self._previous_distance = self._distance
        self._distance = 0
        self._towns = []
        self.add_town(self._start_town)

    def is_distance_shorter_than_previous(self):
        return self._distance < self._previous_distance

    def is_distance_same_than_previous(self):
        return self._distance == self._previous_distance

    def get_last_pheromon_intensity(self):
        return self._last_pheromon_intensity

    def set_last_pheromon_intensity(self, intensity):
        self._last_pheromon_intensity = intensity

    def visited_towns(self, towns):
        for town in towns:
            try:
                self.get_towns().index(town)
            except ValueError:
                return False
        return True