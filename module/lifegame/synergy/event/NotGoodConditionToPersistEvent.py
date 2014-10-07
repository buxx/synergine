from src.synergy.event.ContactEvent import ContactEvent
from module.lifegame.synergy.object.Cell import Cell

class NotGoodConditionToPersistEvent(ContactEvent):
# todo utiliser l'attribut pour Cell
  def filter_objects(self, objects, context):
    filtereds_objects = []
    for obj in objects:
      if isinstance(obj, Cell):
        filtereds_objects.append(obj)
    return filtereds_objects

  def observe(self, obj, context, parameters={}):
    # TODO: implementer un systeme generique pour preciser de quell classe d'obj on parle (pour les concerned objects)
    cell_near_count = 0
    for object_near in parameters['objects_near']:
      if isinstance(object_near, Cell):
        cell_near_count += 1
    if cell_near_count < 2 or cell_near_count > 3:
      self.trigger(obj, context, parameters)
