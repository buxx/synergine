from synergine.core.exceptions import UselessMechanism
from synergine.core.simulation.mechanism.Mechanism import Mechanism
from xyzworld.cst import POSITION


class AroundMechanism(Mechanism):
    """
    Compute near object ids of concerned object.
    """

    def _get_computed_object_event_parameters(self, object_id, context):
        """

        :param object_id: Concerned object id
        :param context: Context object
        :return: Near objects ids: {'objects_ids_near': [0, 1, 2, 3, ...]}
        :rtype: dict
        """

        object_point = context.metas.value.get(POSITION, object_id)
        objects_ids_near = context.get_objects_ids_near_point(object_point, 1)

        # If we not have near object, this mechanism is useless. So we raise a UselessMechanism: Synergine will not
        # run associated events in this case.
        if not objects_ids_near:
            raise UselessMechanism()

        return {'objects_ids_near': objects_ids_near}
