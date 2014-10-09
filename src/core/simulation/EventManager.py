class EventManager():

    def __init__(self):
        self._collections_mechanisms_steps = {}

    def refresh(self, collections):
        for collection in collections:
            self._collections_mechanisms_steps[collection] = self._get_mechanisms_steps_for_collection(collection)

    def _get_mechanisms_steps_for_collection(self, collection):
        collection_mechanisms_steps = []
        for collection_step_actions in collection.get_actions_steps():
            collection_step_events = self._get_events_for_actions(collection_step_actions)
            collection_mechanisms_steps.append(self._get_mechanisms_for_events(collection_step_events))
        return collection_mechanisms_steps

    def _get_events_for_actions(self, actions):
        events_definition = {}
        events = []
        for action in actions:
            action_event_class = action.get_listened_class()
            if action_event_class not in events_definition:
                events_definition[action_event_class] = [action]
            else:
                events_definition[action_event_class].append(action)
        for event_class in events_definition:
            events.append(event_class(events_definition[event_class]))
        return events

    def _get_mechanisms_for_events(self, events):
        mechanisms_definition = {}
        mechanisms = []
        for event in events:
            event_mechanism_class = event.get_mechanism_class()
            if event_mechanism_class not in mechanisms_definition:
                mechanisms_definition[event_mechanism_class] = [event]
            else:
                mechanisms_definition[event_mechanism_class].append(event)
        for event_class in mechanisms_definition:
            mechanisms.append(event_class(mechanisms_definition[event_class]))
        return mechanisms

    def get_collection_mechanisms_steps(self, collection):
        return self._collections_mechanisms_steps[collection]