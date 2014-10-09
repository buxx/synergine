from src.synergy.event.Listener import Listener
from tests.src.event.TooMuchBeansEvent import TooMuchBeansEvent

class TooMuchBeansListener(Listener):

  _listen = TooMuchBeansEvent

  def run(self, collection, context):
    self._obj.beans = 0
