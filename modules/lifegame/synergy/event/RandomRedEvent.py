import random
from synergine.synergy.event.Event import Event
from lifegame.cst import DIED, ALIVE


class RandomRedEvent(Event):
  """
  Illustration of double state usage (concern)
  """

    def concern(self, object_id, context):
        return context.metas.states.have_one(object_id, [ALIVE, DIED])

    def _object_match(self, obj, context, parameters={}):
        return random.randint(0, 50) == 50