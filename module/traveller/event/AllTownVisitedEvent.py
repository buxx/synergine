from synergine.src.synergy.event.Event import Event
from module.traveller.event.TownTasteMechanism import TownTasteMechanism
from module.traveller.synergy.Traveller import Traveller

class AllTownVisitedEvent(Event):
    """
    Le traveller a visité toutes les towns
    """

    def __init__(self, actions):
        super().__init__(actions)
        self._concerneds = [Traveller]
        self._mechanism = TownTasteMechanism