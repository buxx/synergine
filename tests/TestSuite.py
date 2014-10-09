from src.test.TestSuite import TestSuite as BaseTestSuite
from tests.simulation.TestSimulation import TestSimulation
from tests.core.connection.TestTerminal import TestTerminal

class TestSuite(BaseTestSuite):

    def __init__(self):
        super().__init__()
        self.add_test_cases([TestSimulation, TestTerminal])
