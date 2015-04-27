from synergine.synergy.Simulation import Simulation


class MetaStates():
    def __init__(self, list):
        self._list = list

    #  TODO: have_list etc
    def have_list(self, object_id, states):
        for state in states:
            if not self._list.have(Simulation.STATE, object_id, state, allow_empty=True):
                return False
        return True

    def have(self, object_id, state):
        return self.have_list(object_id, [state])

    def dont_have_list(self, object_id, states):
        for state in states:
            if self._list.have(Simulation.STATE, object_id, state, allow_empty=True):
                return False
        return True

    def dont_have(self, object_id, state):
        return self.dont_have_list(object_id, [state])

    def have_one(self, object_id, states):
        for state in states:
            if self._list.have(Simulation.STATE, object_id, state, allow_empty=True):
                return True
        return False

    def dont_have_one(self, object_id, states):
        for state in states:
            if not self._list.have(Simulation.STATE, object_id, state, allow_empty=True):
                return True
        return False

    def add(self, object_id, state):
        self._list.add(Simulation.STATE, object_id, state)

    def add_list(self, object_id, states):
        for state in states:
            self.add(object_id, state)

    def remove(self, object_id, state, allow_empty=False, allow_not_in=False):
        self._list.remove(Simulation.STATE, object_id, state, allow_empty=allow_empty, allow_not_in=allow_not_in)

    def remove_list(self, object_id, states, allow_empty=False, allow_not_in=False):
        for state in states:
            self.remove(object_id, state, allow_empty=allow_empty, allow_not_in=allow_not_in)

    def add_remove(self, object_id, state_add, state_remove, allow_empty=False, allow_not_in=False):
        self.add(object_id, state_add)
        self.remove(object_id, state_remove, allow_empty=allow_empty, allow_not_in=allow_not_in)

    def add_remove_lists(self, objec_id, states_add, states_remove, allow_empty=False, allow_not_in=False):
        for state_add in states_add:
            self.add(objec_id, state_add)
        for state_remove in states_remove:
            self.remove(objec_id, state_remove, allow_empty=allow_empty, allow_not_in=allow_not_in)

