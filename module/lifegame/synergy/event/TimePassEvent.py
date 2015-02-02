from synergine.synergy.event.Event import Event
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation


class TimePassEvent(Event):

  def concern(self, object_id, context):
      return context.metas.list.have(LifeGameSimulation.STATE, object_id, LifeGameSimulation.ALIVE)\
             or context.metas.list.have(LifeGameSimulation.STATE, object_id, LifeGameSimulation.DIED)

  def _object_match(self, obj, context, parameters={}):
      return True
