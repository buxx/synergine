from synergine.synergy.event.Action import Action
from lifegame.synergy.event.GoodConditionToBornEvent import GoodConditionToBornEvent
from lifegame.cst import DIED, ALIVE


class BornAction(Action):
    """
    This action change state of Cell into alive.
    """

    _listen = GoodConditionToBornEvent
    """This action listen the GoodConditionToBornEvent"""

    def run(self, obj, context, synergy_manager):
        obj.set_alive(True)
        # We update states to.
        context.metas.states.add_remove(obj.get_id(), ALIVE, DIED)