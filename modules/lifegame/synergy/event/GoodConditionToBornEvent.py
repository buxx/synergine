from intelligine.core.exceptions import NotConcernedEvent
from xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from synergine.synergy.event.ContactEvent import ContactEvent
from lifegame.cst import ALIVE, COL_DIED


class GoodConditionToBornEvent(ContactEvent):

    concern = COL_DIED

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _prepare(self, object_id, context, parameters={}):
        cell_near_count = 0
        for object_id_near in parameters['objects_ids_near']:
            if context.metas.states.have(object_id_near, ALIVE):
                cell_near_count += 1
        if cell_near_count is 3:
            return parameters
        raise NotConcernedEvent()
