class Mechanism(object):

  def __init__(self, events):
    self._events = events

  def run(self, objects, context):
    for event in self._events:
      for obj in event.filter_objects(objects, context):
        self._run_event(obj, context, event)

  def _run_event(self, obj, context, event):
    event.observe(obj, context)
