from synergine.core.simulation.mechanism.Mechanism import Mechanism
from xyzworld.cst import *


class PositionedArroundMechanism(Mechanism):
    """
    Sur chaque objets on regarde ce qu'il y a autour, si il y a des choses on declenche les
    events
    """

    def _get_object_event_parameters(self, object_id, context):
        object_point = context.metas.value.get(POSITION, object_id)
        objects_ids_near = context.get_objects_ids_by_position_near_point(object_point, 1)
        return {'objects_ids_near_by_positions': objects_ids_near}
