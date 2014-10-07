from src.synergy.event.Listener import Listener
from module.lifegame.synergy.event.NotGoodConditionToPersistEvent import NotGoodConditionToPersistEvent

class RemoveListener(Listener):

  _listen = NotGoodConditionToPersistEvent

  def trigged(self, obj, context, parameters):
    obj.setWill('die')