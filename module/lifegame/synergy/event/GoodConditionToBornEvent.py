from synergine.src.synergy.event.ContactEvent import ContactEvent
from synergine.src.core.simulation.mechanism.ArroundMechanism import ArroundMechanism
from module.lifegame.synergy.object.Cell import Cell
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation

class GoodConditionToBornEvent(ContactEvent):

    def concern(self, obj, context):
        return context.metas.have_state(obj, LifeGameSimulation.DIED)

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _object_match(self, obj, context, parameters={}):
        cell_near_count = 0
        for object_near in parameters['objects_near']:
            if isinstance(object_near, Cell) and object_near.is_alive():
                cell_near_count += 1
        if cell_near_count is 3:
            return True
        return False
