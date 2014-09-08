from src.core.SynergyObjectManager import SynergyObjectManager
from src.core.CycleCalculator import CycleCalculator
from src.core.SpaceDataConnector import SpaceDataConnector
from src.core.config.ConfigurationManager import ConfigurationManager
from src.core.cycle.PipePackage import PipePackage
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
    self._initSyngeries()
    # TODO: Boucle avec FPS etc
    computed_objects = self._cycle_calculator.compute(self._getCyclePackageForCompute())
    print(computed_objects)
    computed_objects = self._cycle_calculator.compute(self._getCyclePackageForCompute())
    print(computed_objects)
    self._cycle_calculator.end()
  
  def _initSyngeries(self):
    for collection_class in self._configuration_manager.getInitialCollectionsClasss():
      self._synergy_object_manager.initCollection(collection=collection_class());
  
  def _getCyclePackageForCompute(self):
    # FUTURE: test si garder le package en attribut de core ameliore les perfs
    pipe_package = PipePackage(self._synergy_object_manager.getComputableObjects())
    pipe_package.setMap({'foo':'map'})
    return pipe_package