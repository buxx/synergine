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
    self._cycle_calculator.compute(self._synergy_object_manager.getComputableObjects())
    pass
  
  def initSyngeries(self):
    from src.synergy.collection.BaseSynergyCollection import BaseSynergyCollection
    self._synergy_object_manager.initCollection(name='BaseSynergyCollection', collection=BaseSynergyCollection());