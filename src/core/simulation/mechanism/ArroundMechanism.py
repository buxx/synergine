from src.core.simulation.mechanism.Mechanism import Mechanism

class ArroundMechanism(Mechanism):
  """
  Sur chaque objets on regarde ce qu'il y a autour, si il y a des choses on declenche les
  events
  """

  # WORK: lier et declencher les events (notion de distance !?)
  def _run_event(self, obj, context, event):
    objects_near = context.getObjectsNearPoint(obj.getPoint(), 1)
    event.observe(obj, context, {'objects_near': objects_near})
