from synergine.synergy.object.SynergyObject import SynergyObject
from tests.src.cst import BEANS


class TestSynergyObject(SynergyObject):

    # TODO: Une méthode set_up parente pour normaliser ?
    def setUp(self, name, beans, coeff):
        self.name = name
        self.beans = beans
        self.coeff = coeff
        self._context.metas.value.set(BEANS, self.get_id(), beans)
