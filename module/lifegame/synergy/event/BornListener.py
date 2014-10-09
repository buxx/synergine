from src.synergy.event.Listener import Listener
from module.lifegame.synergy.event.GoodConditionToBornEvent import GoodConditionToBornEvent

class BornListener(Listener):

  _listen = GoodConditionToBornEvent

  def run(self, collection, context):
    self._obj.set_alive(True)