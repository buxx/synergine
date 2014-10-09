from src.core.simulation.mechanism.Mechanism import Mechanism

class ArroundMechanism(Mechanism):
    """
    Sur chaque objets on regarde ce qu'il y a autour, si il y a des choses on declenche les
    events
    """

    def _get_object_event_parameters(self, obj, context):
        objects_near = context.getObjectsNearPoint(obj.getPoint(), 1)
        return {'objects_near': objects_near}
