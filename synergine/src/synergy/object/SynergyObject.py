from synergine.src.synergy.object.SynergyObjectInterface import SynergyObjectInterface
from synergine.lib.eint import IncrementedNamedInt
from synergine.metas import metas


class SynergyObject(SynergyObjectInterface):

    SIGNAL_CREATED = 'object.created'
    SIGNAL_DELETED = 'object.deleted'

    def __init__(self):
        self._cycle_frequency = 1
        self._id = IncrementedNamedInt.get(self)

    def get_id(self):
        return self._id

    def end_cycle(self):
        pass