from synergine.src.synergy.collection.SynergyCollection import SynergyCollection
from module.traveller.event.MoveAction import MoveAction


class TravellerCollection(SynergyCollection):

    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [MoveAction]
