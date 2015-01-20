from synergine.src.synergy.event.Event import Event
from synergine.src.core.simulation.mechanism.ArroundMechanism import ArroundMechanism
from module.lifegame.synergy.object.Cell import Cell
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
import random


class RandomRedEvent(Event):
  """
  Illustration of double state usage (concern)
  """

    def concern(self, obj, context):
        return context.metas.have_state(obj, LifeGameSimulation.ALIVE)\
               or context.metas.have_state(obj, LifeGameSimulation.DIED)

    def _object_match(self, obj, context, parameters={}):
        if super()._object_match(obj, context, parameters):
            if random.randint(0, 50) == 50:
              return True
        return False
