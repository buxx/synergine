from synergine.core.simulation.mechanism.Mechanism import Mechanism
from xyzworld.cst import POSITION


class ArroundMechanism(Mechanism):
    """
    Sur chaque objets on regarde ce qu'il y a autour, si il y a des choses on declenche les
    events
    """

    def _get_computed_object_event_parameters(self, object_id, context):
        object_point = context.metas.value.get(POSITION, object_id)
        objects_ids_near = context.get_objects_ids_near_point(object_point, 1)
        return {'objects_ids_near': objects_ids_near}
