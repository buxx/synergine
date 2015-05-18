from synergine.core.exceptions import UselessMechanism
from synergine.lib.process.tool import get_chunk


class Mechanism():
    """
    Mechanism prepare data for associated events.
    The principle: One mechanism compute once what multiple events need.
    """

    def __init__(self, events):
        self._events = events
        self._events_parameters = {}

    def run(self, context):
        """

        Prepare new mechanism cycle and return Action according to this mechanism events.

        :param context:
        :return: Actions to run this cycle
        :rtype: list (of Action objects)
        """
        self._events_parameters = {}
        return self._run_events(context)

    def _get_object_parameters(self, object_id, context):
        """

        Return concerned object parameters for event.

        :param object_id: Concerned object if
        :param context: The Context
        :return: parameters who will be used by event
        """
        if object_id not in self._events_parameters:
            self._events_parameters[object_id] = self._get_computed_object_event_parameters(object_id, context)
        return self._events_parameters[object_id]

    def _run_events(self, context):
        """

        Return Action according to this mechanism events.

        :param context: The Context
        :return: list (of Action)
        """
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
        """

        (You must override this method in child-class.)
        Compute concerned object event parameters.


        :param object_id: Concerned object id
        :param context: The Context
        :return: Concerned object event parameters
        """
        return {}
