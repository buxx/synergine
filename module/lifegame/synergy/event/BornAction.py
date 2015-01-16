from synergine.src.synergy.event.Action import Action
from module.lifegame.synergy.event.GoodConditionToBornEvent import GoodConditionToBornEvent

class BornAction(Action):

    _listen = GoodConditionToBornEvent

    def run(self, obj, collection, context):
        obj.set_alive(True)