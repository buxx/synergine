from src.synergy.event.Listener import Listener
from module.lifegame.synergy.event.GoodConditionToBornEvent import GoodConditionToBornEvent

class BornListener(Listener):

  _listen = GoodConditionToBornEvent

  def trigged(self, obj, context, parameters):
    obj.setWill('born')