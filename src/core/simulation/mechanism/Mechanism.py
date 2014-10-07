class Mechanism(object):

  def __init__(self, events):
    self._events = events
    self._events_definitions = {}

  def get_concerned_objects(self, objects):
    concerned_objects = []
    for event in self._events:
      event_objects = event.filter_objects(objects)
      self._events_definitions[event] = event_objects
      concerned_objects.extend(event_objects)
    return concerned_objects

  def run(self, obj, context):
    raise NotImplementedError

  # TODO: La signature de la fonct. est trop specifique a son enfant arroud. Trouver un coppromis de genericite
  def _trigger_events(self, obj, concerneds_objects, context):
    for event in self._events:
      if obj in self._events_definitions[event]:
        event.observe(obj, concerneds_objects, context)