class Mechanism(object):

  def __init__(self, events):
    self._events = events

  def run(self, objects, context):
    for obj in objects:
      self._run_for_object(obj, context)

  def _run_for_object(self, obj, context):
    # Quelque soit le nombre d'event le mechanisme ne calcule qu'une fois les donnees destines aux events
    event_parameters = self._get_object_event_parameters(obj, context)
    for event in self._events:
      event.observe(obj, context, event_parameters)

  def _get_object_event_parameters(self, obj, context):
    return {}
