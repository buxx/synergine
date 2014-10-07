from src.synergy.object import SynergyObject
from src.core.simulation.mechanism.Mechanism import Mechanism

class Event(object):

  _mechanism = Mechanism
  _concerned = SynergyObject

  def __init__(self, listeners):
    self._listeners = listeners

  def getMechanismClass(self):
    return self._mechanism

  def filter_objects(self, objects, context):
    filtereds_objects = []
    for obj in objects:
      if isinstance(obj, self._concerned):
        filtereds_objects.append(obj)
    return filtereds_objects

  def observe(self, obj, context, parameters={}):
    self.trigger(obj, context, parameters)

  def trigger(self, obj, context, parameters={}):
    for listener in self._listeners:
      listener.trigged(obj, context, parameters)