from src.synergy.object import SynergyObject

class Event(object):

  _mechanism = None
  _concerned = SynergyObject

  def __init__(self, listeners):
    self._listeners = listeners

  def getMechanismClass(self):
    return self._mechanism

  def filter_objects(self, objects):
    return objects

  # TODO: La signature de la fonct. est trop specifique a son enfant contact. Trouver un coppromis de genericite
  def observe(self, obj, objects_near, context):
    self.trigger(obj, objects_near, context)

  # TODO: La signature de la fonct. est trop specifique a son enfant contact. Trouver un coppromis de genericite
  def trigger(self, obj, concerneds_objects, context):
    for listener in self._listeners:
      listener.trigged(obj, concerneds_objects, context)