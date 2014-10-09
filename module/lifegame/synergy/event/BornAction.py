from src.synergy.event.Action import Action
from module.lifegame.synergy.event.GoodConditionToBornEvent import GoodConditionToBornEvent

class BornAction(Action):

  _listen = GoodConditionToBornEvent

  def run(self, collection, context):
    self._obj.set_alive(True)