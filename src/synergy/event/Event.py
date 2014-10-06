from src.synergy.object import SynergyObject

class Event(object):

  _mechanism = None
  _concerned = SynergyObject

  def __init__(self, listeners):
    self._listeners = listeners

  def getMechanismClass(self):
    return self._mechanism

  def getConcernedClass(self):
    return self._concerned

  def is_launchable(self, obj, objects_near, context):
    raise NotImplementedError

  def go(self, obj, concerneds_objects, context):
    for listener in self._listeners:
      listener.trigged(obj, concerneds_objects, context)