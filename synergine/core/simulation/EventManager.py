from synergine.core.ActionManager import ActionManager
from synergine.synergy.collection.SynergyCollection import SynergyCollection


class EventManager():
    """
    Manager of collection events.
    """

    def __init__(self, synergy_manager):
        self._synergy_manager = synergy_manager
        self._collections_mechanisms_steps = {}
        self._mechanisms_steps = []
        self._action_manager = ActionManager()

    def refresh(self):
        self._mechanisms_steps = []
        actions = self._get_actions()
        actions_steps = self._action_manager.get_steps_for_actions(actions)
        for step_actions in actions_steps:
            step_events = self._get_events_for_actions(step_actions)
            step_mechanisms = self._get_mechanisms_for_events(step_events)
            self._mechanisms_steps.append(step_mechanisms)

    def _get_actions(self):
        actions = []
        for collection in self._synergy_manager.get_collections():
            for action in collection.get_actions():
                if action not in actions:
                    actions.append(action)
        return actions

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
            event_mechanism_class = event.get_mechanism()
            if event_mechanism_class not in mechanisms_definition:
                mechanisms_definition[event_mechanism_class] = [event]
            else:
                mechanisms_definition[event_mechanism_class].append(event)
        for mechanism_class in mechanisms_definition:
            # Note: Eerur de nommage event_class = mechanism class la
            mechanisms.append(mechanism_class(mechanisms_definition[mechanism_class]))
        return mechanisms

    def get_mechanisms_steps(self):
        return self._mechanisms_steps