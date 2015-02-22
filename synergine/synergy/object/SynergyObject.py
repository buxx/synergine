from synergine.synergy.object.SynergyObjectInterface import SynergyObjectInterface
from synergine.lib.eint import IncrementedNamedInt


class SynergyObject(SynergyObjectInterface):

    SIGNAL_CREATED = 'object.created'
    SIGNAL_DELETED = 'object.deleted'

    def __init__(self, context):
        self._cycle_frequency = 1
        self._id = IncrementedNamedInt.get(self)
        self._context = context

    def get_id(self):
        return self._id

    def end_cycle(self):
        pass