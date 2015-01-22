from synergine.src.synergy.object.SynergyObject import SynergyObject
from synergine.metas import metas
from tests.src.TestSimulation import TestSimulation


class TestSynergyObject(SynergyObject):

    # TODO: Une méthode set_up parente pour normaliser ?
    def setUp(self, name, beans, coeff):
        self.name = name
        self.beans = beans
        self.coeff = coeff
        metas.value.set(TestSimulation.BEANS, self.get_id(), beans)
