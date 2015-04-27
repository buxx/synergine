from synergine.core.simulation.MetaCollections import MetaCollections
from synergine.core.simulation.MetaValue import MetaValue
from synergine.core.simulation.MetaStates import MetaStates
from synergine.core.simulation.MetaSynergyCollections import MetaSynergyCollections


class MetaDatas():
    def __init__(self):
        self.list = MetaCollections()
        self.value = MetaValue()
        self.states = MetaStates(self.list)
        self.collections = MetaSynergyCollections(self.list)

    def reset(self):
        self.list.reset()
        self.value.reset()