import unittest
from synergine.src.test.TestSimulation import TestSimulation as BaseTestSimulation
from tests.src.TestCollection import TestCollection
from tests.src.TestSimulation import TestSimulation as TestSimulationSimulation
from tests.src.TestCollectionConfiguration import TestCollectionConfiguration
from tests.src.TestRunerDisplay import TestRunerDisplay

class TestTerminal(BaseTestSimulation):

    def setUp(self):
        self._connection = TestRunerDisplay()

    def _get_set_up_simulation(self):
        return TestSimulationSimulation([TestCollection(TestCollectionConfiguration())])

    def test_encapsulated_run(self):
        core = self.get_core()
        self.assertTrue(self._connection.have_encapsulated_run())
        self.assertEqual(core.have_to_be_runned_by(), self._connection)