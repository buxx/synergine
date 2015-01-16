from synergine.src.synergy.object import SynergyObject
from synergine.src.core.simulation.mechanism.Mechanism import Mechanism

class Event():

    def __init__(self, actions):
        self._actions = actions
        self._mechanism = Mechanism
        self._concerneds = [SynergyObject]

    def get_mechanism_class(self):
        return self._mechanism

    def observe(self, obj, context, parameters={}):
        active_actions = []
        if self._object_match(obj, context, parameters):
            for action in self._actions:
                active_actions.append(action(obj, parameters))
        return active_actions

    def _object_match(self, obj, context, parameters={}):
        for concerned in self._concerneds:
            if isinstance(obj, concerned):
                return True
        return False