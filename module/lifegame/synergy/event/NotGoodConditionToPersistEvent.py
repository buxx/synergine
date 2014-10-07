from src.synergy.event.ContactEvent import ContactEvent
from src.core.simulation.mechanism.ArroundMechanism import ArroundMechanism
from module.lifegame.synergy.object.Cell import Cell

class NotGoodConditionToPersistEvent(ContactEvent):

  def __init__(self, listeners):
    super(NotGoodConditionToPersistEvent, self).__init__(listeners)
    self._concerneds = [Cell]
    self._mechanism = ArroundMechanism

  def _object_match(self, obj, context, parameters={}):
    if super(NotGoodConditionToPersistEvent, self)._object_match(obj, context, parameters):
      # TODO: implementer un systeme generique pour preciser de quell classe d'obj on parle (pour les concerned objects)
      cell_near_count = 0
      for object_near in parameters['objects_near']:
        if isinstance(object_near, Cell):
          cell_near_count += 1
      if cell_near_count < 2 or cell_near_count > 3:
        return True
    return False