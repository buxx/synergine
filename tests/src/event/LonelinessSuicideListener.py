from src.synergy.event.Listener import Listener
from tests.src.event.LonelinessSuicideEvent import LonelinessSuicideEvent

class LonelinessSuicideListener(Listener):

  _listen = LonelinessSuicideEvent

  def run(self, collection, context):
    collection.remove_object(self._obj)
