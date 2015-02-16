from synergine.synergy.event.Event import Event
from lifegame.cst import DIED, ALIVE


class TimePassEvent(Event):

  def concern(self, object_id, context):
      return context.metas.states.have_one(object_id, [ALIVE, DIED])

  def _object_match(self, obj, context, parameters={}):
      return True
