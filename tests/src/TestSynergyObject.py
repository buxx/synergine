from src.synergy.object.SynergyObject import SynergyObject

class TestSynergyObject(SynergyObject):
  
  # TODO: Une méthode setUp parente pour normaliser ?
  def setUp(self, name, beans, coeff):
    self.name = name
    self.beans = beans
    self.coeff = coeff
