import random

from synergine.synergy.event.Event import Event
from lifegame.synergy.LifeGameSimulation import LifeGameSimulation


class RandomRedEvent(Event):
  """
  Illustration of double state usage (concern)
  """

    def concern(self, object_id, context):
        return context.metas.list.have(LifeGameSimulation.STATE, object_id, LifeGameSimulation.ALIVE)\
               or context.metas.list.have(LifeGameSimulation.STATE, object_id, LifeGameSimulation.DIED)

    def _object_match(self, obj, context, parameters={}):
        return random.randint(0, 50) == 50