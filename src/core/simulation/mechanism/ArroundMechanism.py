from src.core.simulation.mechanism.Mechanism import Mechanism

class ArroundMechanism(Mechanism):
  """
  Sur chaque objets on regarde ce qu'il y a autour, si il y a des choses on declenche les
  events
  """

  # WORK: lier et declencher les events (notion de distance !?)
  def run(self, obj, context): # DEV: Recoi les objets qui le concerne
    objects_near = context.getObjectsNearPoint(obj.getPoint(), 1)
    self._trigger_events(obj, objects_near, context)
