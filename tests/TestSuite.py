from synergine.src.test.TestSuite import TestSuite as BaseTestSuite
from tests.simulation.TestSimulation import TestSimulation
from tests.core.connection.TestTerminal import TestTerminal
from tests.core.TestActionManager import TestActionManager
from tests.core.display.TestZone import TestZone

class TestSuite(BaseTestSuite):

    def __init__(self):
        super().__init__()
        self.add_test_cases([TestZone, TestActionManager, TestSimulation, TestTerminal])
