from src.core.SynergyObjectManager import SynergyObjectManager
from src.core.CycleCalculator import CycleCalculator
from src.core.SpaceDataConnector import SpaceDataConnector
from src.core.config.ConfigurationManager import ConfigurationManager
from lib.factory.factory import Factory
from config import config

class Core(object):
  
  def __init__(self):
    self._configuration_manager = ConfigurationManager(config)
    self._factory = Factory()
    self._synergy_object_manager =  SynergyObjectManager()
    self._cycle_calculator = CycleCalculator()
    self._space_data_connector = SpaceDataConnector()
  
  def run(self):
    self.initSyngeries()
    # TODO: Boucle avec FPS etc
    self._cycle_calculator.compute(self._synergy_object_manager.getComputableObjects())
    self._cycle_calculator.end()
  
  def initSyngeries(self):
    for collection_class in self._configuration_manager.getInitialCollectionsClasss():
      self._synergy_object_manager.initCollection(collection=collection_class());