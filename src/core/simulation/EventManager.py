class EventManager(object):

  def __init__(self):
    self._listeners = []
    self._events = []
    self._mechanisms = []

  def refresh(self, listeners):
    # TODO: Actualiser la liste de mechanismes actifs, a partir des listeners et de leurs events.
    # lier tout ça ...
    self._events = self._get_events_for_listeners(listeners)  # TODO: EventManager a besoin de garder events en attribut ?
    self._mechanisms = self._get_mechanisms_for_events(self._events)

  def _get_events_for_listeners(self, listeners):
    events_definition = {}
    events = []
    for listener in listeners:
      listener_event_class = listener.get_listened_class()
      if listener_event_class not in events_definition:
        events_definition[listener_event_class] = [listener]
      else:
        events_definition[listener_event_class].append(listener)
    for event_class in events_definition:
      events.append(event_class(events_definition[event_class]))
    return events

  def _get_mechanisms_for_events(self, events):
    mechanisms_definition = {}
    mechanisms = []
    for event in events:
      event_mechanism_class = event.getMechanismClass()
      if event_mechanism_class not in mechanisms_definition:
        mechanisms_definition[event_mechanism_class] = [event]
      else:
        mechanisms_definition[event_mechanism_class].append(event)
    for event_class in mechanisms_definition:
      mechanisms.append(event_class(mechanisms_definition[event_class]))
    return mechanisms

  def get_mechanisms(self):
    return self._mechanisms