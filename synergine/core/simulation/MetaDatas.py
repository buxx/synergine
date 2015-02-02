from synergine.core.simulation.MetaCollections import MetaCollections
from synergine.core.simulation.MetaValue import MetaValue


class MetaDatas:

  def __init__(self):
    self.list = MetaCollections()
    self.value = MetaValue()

  def reset(self):
    self.list.reset()
    self.value.reset()