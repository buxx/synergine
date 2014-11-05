from synergine.src.synergy.object.SynergyObject import SynergyObject


class Traveller(SynergyObject):

    def __init__(self):
        super().__init__()
        self._town = None
        self._towns = []

    def _set_town(self, town):
        self._town = town

    def get_town(self):
        return self._town

    def add_town(self, town):
        self._towns.append(town)
        self._set_town(town)
        self.add_trace(town.get_point())

    def get_towns(self):
        return self._towns