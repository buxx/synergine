from synergine.synergy.event.Event import Event
from lifegame.cst import COL_ALL


class TimePassEvent(Event):

  concern = COL_ALL

  def _object_match(self, obj, context, parameters={}):
      return True
