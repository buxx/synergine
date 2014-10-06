class Mechanism(object):

  def __init__(self, events):
    self._events = events

  def get_concerned_objects(self, objects):
    concerned_objects = []
    for obj in objects:
      for event in self._events:
        if isinstance(obj, event.getConcernedClass()):
          concerned_objects.append(obj)
    return concerned_objects

  def run(self, obj, context):
    raise NotImplementedError

  def _trigger_events(self, obj, concerneds_objects, context):
    for event in self._events:
      if event.is_launchable(obj, concerneds_objects, context):
        event.go(obj, concerneds_objects, context)