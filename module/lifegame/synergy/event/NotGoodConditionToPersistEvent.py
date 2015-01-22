from synergine.src.synergy.event.ContactEvent import ContactEvent
from synergine.src.core.simulation.mechanism.ArroundMechanism import ArroundMechanism
from module.lifegame.synergy.object.Cell import Cell
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation


class NotGoodConditionToPersistEvent(ContactEvent):

    def concern(self, object_id, context):
        return context.metas.list.have(LifeGameSimulation.STATE, object_id, LifeGameSimulation.ALIVE)

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _object_match(self, object_id, context, parameters={}):
        cell_near_count = 0
        for object_id_near in parameters['objects_ids_near']:
            # TODO: controler que l'object_near est d'instance Cell (avec un STATE evidemment)
            if context.metas.list.have(LifeGameSimulation.STATE, object_id_near, LifeGameSimulation.ALIVE):
                cell_near_count += 1
        if cell_near_count < 2 or cell_near_count > 3:
            return True
        return False
