from src.synergy.event.Event import Event
from src.core.simulation.mechanism.ArroundMechanism import ArroundMechanism

class ContactEvent(Event):

  _mechanism = ArroundMechanism

  def is_launchable(self, obj, objects_near, context):
    return True