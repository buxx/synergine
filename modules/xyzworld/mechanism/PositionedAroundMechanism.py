from synergine.core.simulation.mechanism.Mechanism import Mechanism
from xyzworld.cst import *


class PositionedAroundMechanism(Mechanism):
    """
    Compute near object ids with position of concerned object.
    """

    def _get_computed_object_event_parameters(self, object_id, context):

        """

        :param object_id: Concerned object id
        :param context: Context object
        :return: Near objects ids, organized by positions:
                 {'objects_ids_near_by_positions': {(z, x, y): [0, 1, 2, ...], ...}}
        :rtype: dict
        """
        object_point = context.metas.value.get(POSITION, object_id)
        objects_ids_near = context.get_objects_ids_by_position_near_point(object_point, 1)
        return {'objects_ids_near_by_positions': objects_ids_near}
