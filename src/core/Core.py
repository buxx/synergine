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
    self._cycle_calculator = CycleCalculator(force_main_process=False) # TODO: debug in conf
    self._space_data_connector = SpaceDataConnector()
  
  def run(self):
    self._initSyngeries()
    # TODO: Boucle avec FPS etc
    for i in range(2):
      self._cycle_calculator.computeCollections(collections=self._synergy_object_manager.getCollections(),\
                                                context=self._getContext())
    self._cycle_calculator.end()
  
  def _initSyngeries(self):
    for collection_class in self._configuration_manager.getInitialCollectionsClasss():
      self._synergy_object_manager.initCollection(collection=collection_class());
  
  def _getContext(self):
    # On construit ici in tableau/objet qui permet au sous processus d'utiliser
    # des objets a jour
    return {'map': {'foo': 'bar'}}
