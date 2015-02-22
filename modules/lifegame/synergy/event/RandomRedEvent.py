import random
from synergine.synergy.event.Event import Event
from lifegame.cst import COL_ALL


class RandomRedEvent(Event):
  """
  Illustration of double state usage (concern)
  """

    concern = COL_ALL

    def _object_match(self, obj, context, parameters={}):
        return random.randint(0, 50) == 50