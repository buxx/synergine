from synergine.src.core.simulation.MetaCollections import MetaCollections
from synergine.src.core.simulation.MetaValue import MetaValue


class MetaDatas:

  def __init__(self):
    self.list = MetaCollections()
    self.value = MetaValue()

  def reset(self):
    self.list.reset()
    self.value.reset()