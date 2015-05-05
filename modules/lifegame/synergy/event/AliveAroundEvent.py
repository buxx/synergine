from synergine.core.exceptions import NotConcernedEvent
from xyzworld.mechanism.AroundMechanism import AroundMechanism
from synergine.synergy.event.ContactEvent import ContactEvent
from lifegame.cst import ALIVE, COL_DIED


class AliveAroundEvent(ContactEvent):
    """
    This class is a refactored class for die and born events.
    """

    def _get_alive_cell_around_count(self, context, parameters):
        cell_near_count = 0
        #  parameters dict is prepared by mechanism
        for object_id_near in parameters['objects_ids_near']:
            if context.metas.states.have(object_id_near, ALIVE):
                cell_near_count += 1
        return cell_near_count