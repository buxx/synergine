from synergine.src.core.SynergyObjectManager import SynergyObjectManager
from synergine.src.core.CycleCalculator import CycleCalculator
from synergine.src.core.SpaceDataConnector import SpaceDataConnector
from synergine.src.core.config.ConfigurationManager import ConfigurationManager
from synergine.src.core.connection.Connector import Connector
from synergine.src.core.cycle.Context import Context
from synergine.lib.factory.factory import Factory
from time import time, sleep


class Core():
    """
    Core of Synergine
    """

    @classmethod
    def start_core(cls, config):
        core = cls(config)
        have_to_be_runned_by = core.have_to_be_runned_by()
        if have_to_be_runned_by:
            have_to_be_runned_by.encapsulate_run(core.run)
        else:
            core.run()

    def __init__(self, config: dict):
        self._configuration_manager = ConfigurationManager(config)
        self._factory = Factory()
        self._synergy_object_manager =    SynergyObjectManager(self._configuration_manager.get('simulations'))
        self._cycle_calculator = CycleCalculator(self._synergy_object_manager, force_main_process=self._configuration_manager.get('engine.debug.mainprocess')) # TODO: debug in conf
        self._space_data_connector = SpaceDataConnector()
        self._last_cycle_time = time()
        self._maxfps = self._configuration_manager.get('engine.fpsmax')
        self._connector = Connector(self._configuration_manager.get('connections'), self._synergy_object_manager)
        self._context = Context(self._synergy_object_manager)

    def run(self, screen = None): # TODO: screen: Rendre pour le cas ou le display n'a pas besoin de ca
        if screen:
            self._connector.send_screen_to_connection(screen)
        self._run_connecteds()
        self._wait_for_next_cycle()
        for i in self._configuration_manager.get('engine.debug.cycles', True): # TODO: True ne marche dans la boucle
            self._update_last_cycle_time()
            self._context.update()
            self._cycle_calculator.compute(self._context)
            self._run_connecteds()
            self._wait_for_next_cycle()
        self._end()

    def _end(self):
        self._cycle_calculator.end()
        self._connector.terminate()

    def _update_last_cycle_time(self):
        self._last_cycle_time = time()

    def _wait_for_next_cycle(self):
        if self._maxfps is not True:
            sleep(max(1./self._maxfps - (time() - self._last_cycle_time), 0))

    def _run_connecteds(self):
        self._connector.cycle()

    def have_to_be_runned_by(self):
        return self._connector.get_connection_who_have_to_run_core()
