from synergine.src.synergy.collection.SynergyCollection import SynergyCollection


class TravellerCollection(SynergyCollection):

    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = []
