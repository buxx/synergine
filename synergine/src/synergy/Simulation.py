from synergine.lib.eint import IncrementedNamedInt


class Simulation():

    STATE = IncrementedNamedInt.get('simulation.state')

    def __init__(self, collections):
        self._collections = collections

    def get_collections(self):
        return self._collections

    def start_cycle(self, context):
        pass

    def end_cycle(self, context):
        pass
