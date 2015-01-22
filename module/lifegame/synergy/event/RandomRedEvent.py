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
        return context.metas.list.have(LifeGameSimulation.STATE, obj, LifeGameSimulation.ALIVE)\
               or context.metas.list(LifeGameSimulation.STATE, obj, LifeGameSimulation.DIED)

    def _object_match(self, obj, context, parameters={}):
        return random.randint(0, 50) == 50