from src.core.SynergyObjectManager import SynergyObjectManager
from src.core.CycleCalculator import CycleCalculator
from src.core.SpaceDataConnector import SpaceDataConnector

class Core(object):
  
  def __init__(self):
    self._synergy_object_manager =  SynergyObjectManager()
    self._cycle_calculator = CycleCalculator()
    self._space_data_connector = SpaceDataConnector()
  
  def run(self):
    self.initSyngeries()
    # TODO: Boucle avec FPS etc
    self._cycle_calculator.compute(self._synergy_object_manager.getComputableObjects())
    self._cycle_calculator.end()
  
  def initSyngeries(self):
    # TODO: systeme de config et d'import auto
    from src.synergy.collection.BaseSynergyCollection import BaseSynergyCollection
    collection_class = BaseSynergyCollection
    self._synergy_object_manager.initCollection(collection=collection_class());