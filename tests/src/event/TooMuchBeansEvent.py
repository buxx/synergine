from src.synergy.event.Event import Event
from tests.src.TestSynergyObject import TestSynergyObject

class TooMuchBeansEvent(Event):

  #_concerned = TestSynergyObject

  def filter_objects(self, objects, context):
    filtereds_objects = []
    for obj in objects:
      if isinstance(obj, TestSynergyObject) and obj.beans > 10000000:
        filtereds_objects.append(obj)
    return filtereds_objects

  def observe(self, obj, context, parameters={}):
    self.trigger(obj, context, parameters)