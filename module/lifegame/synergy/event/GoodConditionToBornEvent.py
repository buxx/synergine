from module.xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from synergine.synergy.event.ContactEvent import ContactEvent
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation

class GoodConditionToBornEvent(ContactEvent):

    def concern(self, object_id, context):
        return context.metas.list.have(LifeGameSimulation.STATE, object_id, LifeGameSimulation.DIED)

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _object_match(self, object_id, context, parameters={}):
        cell_near_count = 0
        for object_id_near in parameters['objects_ids_near']:
            if context.metas.list.have(LifeGameSimulation.STATE, object_id_near, LifeGameSimulation.ALIVE):
                cell_near_count += 1
        if cell_near_count is 3:
            return True
        return False
