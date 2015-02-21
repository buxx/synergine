from xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from synergine.synergy.event.ContactEvent import ContactEvent
from lifegame.cst import ALIVE, COL_ALIVE


class NotGoodConditionToPersistEvent(ContactEvent):

    concern = COL_ALIVE

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _object_match(self, object_id, context, parameters={}):
        cell_near_count = 0
        for object_id_near in parameters['objects_ids_near']:
            if context.metas.states.have(object_id_near, ALIVE):
                cell_near_count += 1
        if cell_near_count < 2 or cell_near_count > 3:
            return True
        return False
