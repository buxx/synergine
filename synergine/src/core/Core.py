from synergine.src.core.SynergyObjectManager import SynergyObjectManager
from synergine.src.core.CycleCalculator import CycleCalculator
from synergine.src.core.SpaceDataConnector import SpaceDataConnector
from synergine.src.core.config.ConfigurationManager import ConfigurationManager
from synergine.src.core.connection.Connector import Connector
from synergine.src.core.cycle.Context import Context
from synergine.lib.factory.factory import Factory
from time import time, sleep
from os import listdir
from os.path import isdir, join as join_path
from importlib import import_module


class Core():
    """
    Core of Synergine
    """

    _configuration_manager = ConfigurationManager()

    @classmethod
    def start_core(cls, config, modules_path='module'):  # TODO: path en relatif !
        core = cls(config, modules_path)
        have_to_be_runned_by = core.have_to_be_runned_by()
        if have_to_be_runned_by:
            have_to_be_runned_by.encapsulate_run(core.run)
        else:
            core.run()

    @classmethod
    def get_configuration_manager(cls):
        return cls._configuration_manager

    def __init__(self, config: dict, modules_path):
        self._load_configuration(modules_path, config)
        self._factory = Factory()
        self._synergy_object_manager =    SynergyObjectManager(self._configuration_manager.get('simulations'))
        self._cycle_calculator = CycleCalculator(self._synergy_object_manager, force_main_process=self._configuration_manager.get('engine.debug.mainprocess')) # TODO: debug in conf
        self._space_data_connector = SpaceDataConnector()
        self._last_cycle_time = time()
        self._maxfps = self._configuration_manager.get('engine.fpsmax')

        # TODO: Gestionnaire/Factory pour la construction
        context_class = self._configuration_manager.get('app.classes.Context', Context)
        self._context = context_class(self._synergy_object_manager)

        self._connector = Connector(self._synergy_object_manager, self._context)
        self._initialize_connecteds()


    def _load_configuration(self, modules_path, app_config):
        modules = [file for file in listdir(modules_path) if isdir(join_path(modules_path, file))]
        for module in modules:
            try:
                module_config_module = import_module(modules_path+'.'+module+'.config')
                self._configuration_manager.load(module_config_module.config)
            except ImportError:
                pass
        self._configuration_manager.load(app_config)

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

    def _initialize_connecteds(self):
        self._connector.initialize_terminals(self._configuration_manager.get('connections'), self._configuration_manager)

    def _run_connecteds(self):
        self._connector.cycle()

    def have_to_be_runned_by(self):
        return self._connector.get_connection_who_have_to_run_core()

    def get_terminal(self, terminal_name):
        return self._connector.get_terminal(terminal_name)