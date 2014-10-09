from src.synergy.event.Event import Event
from src.core.simulation.mechanism.ArroundMechanism import ArroundMechanism

class ContactEvent(Event):

  def __init__(self, actions):
    super(ContactEvent, self).__init__(actions)
    self._concerneds = [ArroundMechanism]
