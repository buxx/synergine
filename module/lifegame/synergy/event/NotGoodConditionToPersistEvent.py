from src.synergy.event.ContactEvent import ContactEvent
from module.lifegame.synergy.object.Cell import Cell

class NotGoodConditionToPersistEvent(ContactEvent):

  _concerned = Cell

  def is_launchable(self, obj, objects_near, context):
    # TODO: implementer un systeme generique pour preciser de quell classe d'obj on parle (pour les concerned objects)
    cell_near_count = 0
    for object_near in objects_near:
      if isinstance(object_near, Cell):
        cell_near_count += 1
    if cell_near_count < 2 or cell_near_count > 3:
      return True
    return False