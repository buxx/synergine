from synergine.src.synergy.object.SynergyObject import SynergyObject

class TestSynergyObject(SynergyObject):

    # TODO: Une méthode set_up parente pour normaliser ?
    def setUp(self, name, beans, coeff):
        self.name = name
        self.beans = beans
        self.coeff = coeff
