from src.synergy.event.Listener import Listener
from tests.src.event.TooMuchBeansEvent import TooMuchBeansEvent

class TooMuchBeansListener(Listener):

  _listen = TooMuchBeansEvent

  def trigged(self, obj, context, parameters):
    obj.beans = 0  # TODO: On doit avoir une Action (future) ici pour que ce soit traite en dehors du processus
