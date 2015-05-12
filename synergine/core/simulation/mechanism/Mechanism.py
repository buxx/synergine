from synergine.core.exceptions import UselessMechanism
from synergine.lib.process.tool import get_chunk


class Mechanism():
    """
    A mechanism is an algorithm who run event with some prepared data.
    These data will be prepared for each SynergyObject one time and can
    be gived to x events without re compte them
    """

    def __init__(self, events):
        self._events = events
        self._events_parameters = {}

    def run(self, context):
        self._events_parameters = {}
        return self._run_events(context)

    def _get_object_parameters(self, object_id, context):
        if object_id not in self._events_parameters:
            self._events_parameters[object_id] = self._get_computed_object_event_parameters(object_id, context)
        return self._events_parameters[object_id]

    def _run_events(self, context):
        actions = []
        for event in self._events:
            if context.get_cycle() % event.get_each_cycle() == 0:
                concerned_objects_ids = get_chunk(context.get_total_chunk(),
                                                  context.get_current_chunk_position(),
                                                  context.metas.collections.get(event.get_concern(), allow_empty=True))
                for object_id in concerned_objects_ids:
                    try:
                        event_parameters = self._get_object_parameters(object_id, context)
                        event_actions = event.observe(object_id, context, event_parameters)
                        for event_action in event_actions:
                            actions.append(event_action)
                    except UselessMechanism:
                        pass # If mechanism useless on this object, don't observe.
        return actions

    def _get_computed_object_event_parameters(self, object_id, context):
        return {}
