from synergine.lib.eint import IncrementedNamedInt


class Simulation():

    STATE = IncrementedNamedInt.get('simulation.state')

    def __init__(self, collections):
        self._collections = collections

    def connect_actions_signals(self, Signals):
        pass

    def get_collections(self):
        return self._collections
