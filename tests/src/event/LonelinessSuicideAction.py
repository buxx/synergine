from src.synergy.event.Action import Action
from tests.src.event.LonelinessSuicideEvent import LonelinessSuicideEvent

class LonelinessSuicideAction(Action):

  _listen = LonelinessSuicideEvent

  def run(self, collection, context):
    collection.remove_object(self._obj)
