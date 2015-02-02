class Mechanism():
    """
    A mechanism is an algorithm who run event with some prepared data.
    These data will be prepared for each SynergyObject one time and can
    be gived to x events without re compte them
    """

    def __init__(self, events):
        self._events = events

        # TODO: ailleurs
        # Relation between event and it's concerned "model"
        self._events_concerneds = {}
        for event in self._events:
          if event.concern not in self._events_concerneds:
            self._events_concerneds[event.concern] = []
          self._events_concerneds[event.concern].append(event)

        self._events_parameters = {}

    def _get_events_objects_collections(self, objects_ids, context):
      """
      Prepare one object lisft for each event's concerned objects
      :param objects:
      :return:
      """
      # TODO: Ailleurs non ?
      events_objects_ids_collections = {'__all__': []}
      for concern in self._events_concerneds:
        events_objects_ids_collections[concern] = []
        for object_id in objects_ids:
          if concern(object_id=object_id, context=context):
            events_objects_ids_collections[concern].append(object_id)
            events_objects_ids_collections['__all__'].append(object_id)  # TODO: Si il y a deux ou + actions ?
          # # Pour le moment on gere "un des state"
          # for state in concern:
          #   if context.metas.have_state(obj, state):
          #     events_objects_ids_collections[concern].append(obj)
          #     events_objects_ids_collections['__all__'].append(obj)
      return events_objects_ids_collections

    def run(self, objects_ids, context):
        # TODO: prefiltre sur les objets avec ce que les events veulents:
        # - concerneds (que les concerneds soient pioches dans liste fabrique avec ci-dessous)
        # - idee: les events liste un id (const) de 'rangement' (ex: cellules vivantes, cellules mortes)
        events_objects_ids_collections = self._get_events_objects_collections(objects_ids, context)
        self._prepare_objects_parameters(events_objects_ids_collections['__all__'], context)
        return self._run_events(events_objects_ids_collections, context)

    def _prepare_objects_parameters(self, objects, context):
        # Quelque soit le nombre d'event le mechanisme ne calcule qu'une fois les donnees destines aux events
        self._events_parameters = {}
        for obj in objects:
            self._events_parameters[obj] = self._get_object_event_parameters(obj, context)

    def _run_events(self, events_objects_ids_collections, context):
        actions = []
        for event in self._events:
            concerned_objects_ids = events_objects_ids_collections[event.concern]
            for object_id in concerned_objects_ids:
                event_actions = event.observe(object_id, context, self._events_parameters[object_id])
                for event_action in event_actions:
                    actions.append(event_action)
        return actions

    def _get_object_event_parameters(self, object_id, context):
        return {}
