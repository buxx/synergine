from src.synergy.event.Event import Event
from tests.src.TestSynergyObject import TestSynergyObject

class LonelinessSuicideEvent(Event):

  #_concerned = TestSynergyObject

  def filter_objects(self, objects, context):
    filtereds_objects = []
    for obj in objects:
      if isinstance(obj, TestSynergyObject):
        friends_with_beans_count = 0
        for collection in context.getCollections():
          for friend in collection.getObjects():
            if friend.beans > 1:
              friends_with_beans_count += 1
        if friends_with_beans_count == 0:
          filtereds_objects.append(obj)
    return filtereds_objects

  def observe(self, obj, context, parameters={}):
    self.trigger(obj, context, parameters)