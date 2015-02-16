from synergine.synergy.Simulation import Simulation

class MetaStates():

    def __init__(self, list):
        self._list = list

    def have(self, object_id, states):
        for state in states:
            if not self._list.have(Simulation.STATE, object_id, state):
                return False
        return True

    def dont_have(self, object_id, states):
        for state in states:
            if self._list.have(Simulation.STATE, object_id, state):
                return False
        return True

    def have_one(self, object_id, states):
        for state in states:
            if self._list.have(Simulation.STATE, object_id, state):
                return True
        return False

    def dont_have_one(self, object_id, states):
        for state in states:
            if not self._list.have(Simulation.STATE, object_id, state):
                return True
        return False

    def add(self, object_id, state):
        self._list.add(Simulation.STATE, object_id, state)

    def remove(self, object_id, state):
        self._list.remove(Simulation.STATE, object_id, state)

