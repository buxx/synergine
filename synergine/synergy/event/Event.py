from synergine.core.exceptions import NotConcernedEvent
from synergine.core.simulation.mechanism.Mechanism import Mechanism


class Event():

    _mechanism = Mechanism
    _concern = None
    _each_cycle = 1

    def __init__(self, actions):
        self._actions = actions

    @classmethod
    def get_mechanism(cls):
        return cls._mechanism

    @classmethod
    def get_concern(cls):
        return cls._concern

    @classmethod
    def get_each_cycle(cls):
        return cls._each_cycle

    def observe(self, object_id, context, parameters={}):
        active_actions = []
        try:
            parameters = self._prepare(object_id, context, parameters)
            for action in self._actions:
                action_object = action(object_id, parameters)
                active_actions.append(action_object)
        except NotConcernedEvent:
            pass  # Object not concerned by this event

        return active_actions

    def _prepare(self, object_id, context, parameters={}):
        raise NotImplementedError()