from synergine.src.synergy.event.Event import Event
from synergine.src.core.simulation.mechanism.ArroundMechanism import ArroundMechanism

class ContactEvent(Event):

    def __init__(self, actions):
        super().__init__(actions)
        #self._concerneds = [ArroundMechanism]  # TODO: Y a erreur la non ?
