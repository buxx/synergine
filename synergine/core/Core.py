from synergine.core.SynergyObjectManager import SynergyObjectManager
from synergine.core.CycleCalculator import CycleCalculator
from synergine.core.SpaceDataConnector import SpaceDataConnector
from synergine.core.config.ConfigurationManager import ConfigurationManager
from synergine.core.connection.Connector import Connector
from synergine.lib.factory.factory import Factory
from synergine.core.cycle.Context import Context
from time import time, sleep
from os import listdir
from os.path import isdir, join as join_path
from importlib import import_module
from synergine.core.Signals import Signals


class Core():
    """
    Core of Synergine
    Manage cycle calculator, terminals, ...
    """

    _configuration_manager = ConfigurationManager()

    @classmethod
    def start_core(cls, config, modules_path=None):
        core = cls(config, modules_path)
        have_to_be_runned_by = core.have_to_be_runned_by()
        if have_to_be_runned_by:
            have_to_be_runned_by.encapsulate_run(core.run)
        else:
            core.run()

    @classmethod
    def get_configuration_manager(cls):
        return cls._configuration_manager

    def __init__(self, config: dict, modules_path=None):
        """

        :param config: dict containing the config. Will be used to instanciate ConfigurationManager)
        :param modules_path: path of modules. To retrieve module config
        TODO: obsolete ?
        :return: Core
        """
        self._load_configuration(modules_path, config)
        self._context = self._configuration_manager.get('app.classes.Context', Context)()
        self._context.metas.reset()
        Signals.reset()
        self._factory = Factory()
        self._synergy_object_manager = SynergyObjectManager(self._configuration_manager.get('simulations'),
                                                            self._context)
        self._cycle_calculator = CycleCalculator(self._context,
                                                 self._synergy_object_manager,
                                                 self.get_configuration_manager(),
                                                 force_main_process=self._configuration_manager.get(
                                                     'engine.debug.mainprocess', False))
        self._space_data_connector = SpaceDataConnector()
        self._last_cycle_time = time()
        self._maxfps = self._configuration_manager.get('engine.fpsmax')
        self._connector = Connector(self._synergy_object_manager, self._context)
        self._initialize_connecteds()

    def _load_configuration(self, modules_path, app_config):
        if modules_path:
            modules = [file for file in listdir(modules_path) if isdir(join_path(modules_path, file))]
            for module in modules:
                try:
                    module_config_module = import_module(modules_path + '.' + module + '.config')
                    self._configuration_manager.load(module_config_module.config)
                except ImportError:
                    pass
        self._configuration_manager.load(app_config)

    def run(self, screen=None):
        if screen:
            self._connector.send_screen_to_connection(screen)
        self._run_connecteds()
        self._wait_for_next_cycle()

        cycles = self._configuration_manager.get('engine.debug.cycles', -1)
        finish = False
        if cycles is 0:
            finish = True
        while not finish:

            self._update_last_cycle_time()
            # start_time = time()
            actions_done = self._cycle_calculator.compute()
            self._run_connecteds(actions_done)
            # print(time() - start_time)
            self._wait_for_next_cycle()

            if self._cycle_calculator.get_cycle() >= cycles and cycles is not -1:
                finish = True

        self._end()

    def _end(self):
        self._cycle_calculator.end()
        self._connector.terminate()

    def _update_last_cycle_time(self):
        self._last_cycle_time = time()

    def _wait_for_next_cycle(self):
        if self._maxfps is not True:
            sleep(max(1. / self._maxfps - (time() - self._last_cycle_time), 0))

    def _initialize_connecteds(self):
        self._connector.initialize_terminals(self._configuration_manager.get('connections'),
                                             self._configuration_manager)

    def _run_connecteds(self, actions_done=[]):
        self._connector.cycle(actions_done)

    def have_to_be_runned_by(self):
        return self._connector.get_connection_who_have_to_run_core()

    def get_terminal(self, terminal_name):
        return self._connector.get_terminal(terminal_name)