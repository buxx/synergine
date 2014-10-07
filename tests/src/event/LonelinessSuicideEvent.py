from src.synergy.event.Event import Event
from tests.src.TestSynergyObject import TestSynergyObject

class LonelinessSuicideEvent(Event):

  def __init__(self, listeners):
    super(LonelinessSuicideEvent, self).__init__(listeners)
    self._concerneds = [TestSynergyObject]

  def _object_match(self, obj, context, parameters={}):
    if super(LonelinessSuicideEvent, self)._object_match(obj, context, parameters):
      return not self._has_friends_with_beans(obj, context)
    return False

  def _has_friends_with_beans(self, obj, context):
    friends_with_beans_count = 0
    # TODO: .getCollections: Pas adapte si d'autres collections dans la simu !
    for collection in context.getCollections():
      for friend in collection.getObjects():
        if friend.beans > 1:
          friends_with_beans_count += 1
    if friends_with_beans_count == 0:
      return False
    return True
