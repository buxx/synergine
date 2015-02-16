from synergine.core.simulation.MetaCollections import MetaCollections
from synergine.core.simulation.MetaValue import MetaValue
from synergine.core.simulation.MetaStates import MetaStates


class MetaDatas:

  def __init__(self):
    self.list = MetaCollections()
    self.value = MetaValue()
    self.states = MetaStates(self.list)

  def reset(self):
    self.list.reset()
    self.value.reset()