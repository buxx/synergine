from src.synergy.event.Listener import Listener
from module.lifegame.synergy.event.NotGoodConditionToPersistEvent import NotGoodConditionToPersistEvent

class DieListener(Listener):

  _listen = NotGoodConditionToPersistEvent

  def run(self, collection, context):
    self._obj.set_alive(False)