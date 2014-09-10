from src.core.SynergyObjectManager import SynergyObjectManager
from src.core.CycleCalculator import CycleCalculator
from src.core.SpaceDataConnector import SpaceDataConnector
from src.core.config.ConfigurationManager import ConfigurationManager
from src.core.display.DisplayConnector import DisplayConnector
from src.core.cycle.Context import Context
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
    self._maxfps = self._configuration_manager.get('engine.fpsmax')
    self._display_connector = DisplayConnector(self._getDisplaysToConnect())
    self._context = Context(self._synergy_object_manager)
  
  def _getDisplaysToConnect(self):
    displays = []
    for display_class in self._configuration_manager.get('display.displays'):
      displays.append(display_class())
    return displays
  
  def run(self):
    self._initSyngeries()
    for i in range(100): # TODO: remplacer la valeur de test 100 par qqch qui surveille l'ordre d'arret
      self._updateLastCycleTime()
      self._cycle_calculator.computeCollections(collections=self._synergy_object_manager.getCollections(),\
                                                context=self._getContext())
      self._runDisplay()
      self._waitForNextCycle()
    self._cycle_calculator.end()
  
  def _updateLastCycleTime(self):
    self._last_cycle_time = time()
  
  def _waitForNextCycle(self):
    sleep(max(1./self._maxfps - (time() - self._last_cycle_time), 0))
  
  def _initSyngeries(self):
    for collection_class in self._configuration_manager.get('simulation.collections'):
      self._synergy_object_manager.initCollection(collection=collection_class());
  
  def _getContext(self):
    # On construit ici in tableau/objet qui permet au sous processus d'utiliser
    # des objets a jour
    self._context.update()
    return self._context
  
  def _runDisplay(self):
    # 1: Ici on recup les donnees des objets AFFICHABLE (etre generique bien sur)
    # 2: penser a implementer que les objets informe de si ils sont a redessiner ou non
    # 3: Si dessein progressif: garder a l'esprit qu'il faudra l'ancienne pos. d'un
    # objet pour leffacer avant de le r edessiner
    # TODO: Ne le faire que max 25 fps (issue de config)
    self._display_connector.prepare(self._synergy_object_manager)
    self._display_connector.cycle()
  