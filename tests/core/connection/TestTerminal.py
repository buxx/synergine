import unittest
from src.test.TestSimulation import TestSimulation as BaseTestSimulation
from tests.src.TestCollection import TestCollection
from tests.src.TestSimulation import TestSimulation as TestSimulationSimulation
from tests.src.TestCollectionConfiguration import TestCollectionConfiguration
from tests.src.TestRunerDisplay import TestRunerDisplay

class TestTerminal(BaseTestSimulation):

    def setUp(self):
        self._connection = TestRunerDisplay()

    def _getSetUpSimulation(self):
        return TestSimulationSimulation([TestCollection(TestCollectionConfiguration())])

    def test_encapsulated_run(self):
        core = self.getCore()
        self.assertTrue(self._connection.haveEncapsulatedRun())
        self.assertEqual(core.haveToBeRunnedBy(), self._connection)