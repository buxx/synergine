from synergine.synergy.event.Action import Action
from lifegame.synergy.event.GoodConditionToBornEvent import GoodConditionToBornEvent


class BornAction(Action):
    """
    This action change state of Cell into alive.
    """

    _listen = GoodConditionToBornEvent
    """This action listen the GoodConditionToBornEvent"""

    def run(self, obj, context, synergy_manager):
        obj.set_alive(True)