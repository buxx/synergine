from synergine.synergy.object import SynergyObject
from synergine.core.simulation.mechanism.Mechanism import Mechanism

class Event():

    def concern(self, object_id, context):
      raise NotImplementedError()

    def __init__(self, actions):
        self._actions = actions
        self._mechanism = Mechanism

    def get_mechanism_class(self):
        return self._mechanism

    def observe(self, object_id, context, parameters={}):
        active_actions = []
        if self._object_match(object_id, context, parameters):
            for action in self._actions:
                active_actions.append(action(object_id, parameters))
        return active_actions

    def _object_match(self, object_id, context, parameters={}):
        raise NotImplementedError()