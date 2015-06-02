import unittest
from synergine.test.TestSimulation import TestSimulation as BaseTestSimulation
from tests.src.TestCollection import TestCollection
from tests.src.TestSimulation import TestSimulation as TestSimulationSimulation
from tests.src.TestCollectionConfiguration import TestCollectionConfiguration
from tests.src.TestRunerDisplay import TestRunerDisplay

class TestTerminal(BaseTestSimulation):

    def setUp(self):
        self._connection = TestRunerDisplay

    def _get_set_up_simulations(self):
        return [TestSimulationSimulation([TestCollection(TestCollectionConfiguration())])]

    def test_encapsulated_run(self):
        core = self.get_core()
        self.assertTrue(core.get_terminal(self._connection.get_name()).have_encapsulated_run())
        self.assertEqual(core.have_to_be_runned_by().get_name(), self._connection.get_name())