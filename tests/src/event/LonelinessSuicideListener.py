from src.synergy.event.Listener import Listener
from tests.src.event.LonelinessSuicideEvent import LonelinessSuicideEvent

class LonelinessSuicideListener(Listener):

  _listen = LonelinessSuicideEvent

  def trigged(self, obj, context, parameters):
    obj.setWill('die')  # TODO: On doit avoir une Action (future) ici pour que ce soit traite en dehors du processus
