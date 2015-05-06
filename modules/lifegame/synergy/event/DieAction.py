from synergine.synergy.event.Action import Action
from lifegame.synergy.event.NotGoodConditionToPersistEvent import NotGoodConditionToPersistEvent


class DieAction(Action):
    """
    This action change state of Cell into died.
    """

    _listen = NotGoodConditionToPersistEvent
    """This action listen the NotGoodConditionToPersistEvent"""

    def run(self, obj, context, synergy_manager):
        obj.set_alive(False)