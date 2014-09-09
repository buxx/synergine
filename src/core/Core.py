from src.core.SynergyObjectManager import SynergyObjectManager
from src.core.CycleCalculator import CycleCalculator
from src.core.SpaceDataConnector import SpaceDataConnector
from src.core.config.ConfigurationManager import ConfigurationManager
from lib.factory.factory import Factory
from time import time, sleep
from config import config

class Core(object):
  
  def __init__(self):
    self._configuration_manager = ConfigurationManager(config)
    self._factory = Factory()
    self._synergy_object_manager =  SynergyObjectManager()
    self._cycle_calculator = CycleCalculator(force_main_process=False) # TODO: debug in conf
    self._space_data_connector = SpaceDataConnector()
    self._last_cycle_time = time()
    self._maxfps = self._configuration_manager.getMaxFpsEngine()
  
  def run(self):
    self._initSyngeries()
    for i in range(100): # TODO: remplacer la valeur de test 100 par qqch qui surveille l'ordre d'arret
      self._updateLastCycleTime()
      self._cycle_calculator.computeCollections(collections=self._synergy_object_manager.getCollections(),\
                                                context=self._getContext())
      self._waitForNextCycle()
    self._cycle_calculator.end()
  
  def _updateLastCycleTime(self):
    self._last_cycle_time = time()
  
  def _waitForNextCycle(self):
    sleep(max(1./self._maxfps - (time() - self._last_cycle_time), 0))
  
  def _initSyngeries(self):
    for collection_class in self._configuration_manager.getInitialCollectionsClasss():
      self._synergy_object_manager.initCollection(collection=collection_class());
  
  def _getContext(self):
    # On construit ici in tableau/objet qui permet au sous processus d'utiliser
    # des objets a jour
    return {'map': {'foo': 'bar'}}
