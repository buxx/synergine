import unittest
from synergine.core.Core import Core
from synergine.test.TestTerminal import TestTerminal

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self._connection = TestTerminal

    def _get_set_up_simulation(self):
        raise NotImplementedError

    def _get_core_configuration(self, cycles, main_process = True):
        return {
            'engine': {
                'fpsmax': True,
                'debug': {
                    'mainprocess': main_process,
                    'cycles': cycles
                }
            },
            'simulations' : [self._get_set_up_simulation()],
            'connections': [self._connection]
        }

    def get_core(self, cycles=0, main_process=True):
        #
        #
        core = Core(self._get_core_configuration(cycles, main_process), 'modules')
        have_to_be_runned_by = core.have_to_be_runned_by()
        if have_to_be_runned_by:
            have_to_be_runned_by.encapsulate_run(core.run)
        return core

    def _get_synergy_object_manager_for_cycle(self, cycles, main_process=True):
        core = self.get_core(cycles, main_process)
        core.run()
        return core.get_terminal(self._connection.get_name()).get_synergy_object_manager()
