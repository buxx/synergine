from src.core.SynergyObjectManager import SynergyObjectManager
from src.core.CycleCalculator import CycleCalculator
from src.core.SpaceDataConnector import SpaceDataConnector
from src.core.config.ConfigurationManager import ConfigurationManager
from src.core.connection.Connector import Connector
from src.core.cycle.Context import Context
from lib.factory.factory import Factory
from time import time, sleep

class Core():
  
  def __init__(self, config):
    self._configuration_manager = ConfigurationManager(config)
    self._factory = Factory()
    self._synergy_object_manager =  SynergyObjectManager(self._configuration_manager.get('simulations'))
    self._cycle_calculator = CycleCalculator(self._synergy_object_manager, force_main_process=self._configuration_manager.get('engine.debug.mainprocess')) # TODO: debug in conf
    self._space_data_connector = SpaceDataConnector()
    self._last_cycle_time = time()
    self._maxfps = self._configuration_manager.get('engine.fpsmax')
    self._connector = Connector(self._configuration_manager.get('connections'))
    self._context = Context(self._synergy_object_manager)
  
  def run(self, screen = None): # TODO: screen: Rendre pour le cas ou le display n'a pas besoin de ca
    if screen:
      self._connector.sendScreenToConnection(screen)
    self._runConnecteds()
    self._waitForNextCycle()
    for i in self._configuration_manager.get('engine.debug.cycles', True): # TODO: True ne marche dans la boucle
      self._updateLastCycleTime()
      self._context.update()
      self._cycle_calculator.compute(self._context)
      self._runConnecteds()
      self._waitForNextCycle()
    self._end()
  
  def _end(self):
    self._cycle_calculator.end()
    self._connector.terminate()
  
  def _updateLastCycleTime(self):
    self._last_cycle_time = time()
  
  def _waitForNextCycle(self):
    if self._maxfps is not True:
      sleep(max(1./self._maxfps - (time() - self._last_cycle_time), 0))
  
  def _runConnecteds(self):
    self._connector.prepare(self._synergy_object_manager) # TODO: estce necessaire de redonner l'objet ?
    self._connector.cycle()
  
  def haveToBeRunnedBy(self):
    return self._connector.getConnectionWhoHaveToRunCore()
  