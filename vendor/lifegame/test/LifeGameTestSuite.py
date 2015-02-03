from synergine.test.TestSuite import TestSuite
from lifegame.test.simulation.TestLifeGameSimulation import TestLifeGameSimulation
from lifegame.test.display.TestVisualisation import TestVisualisation

class LifeGameTestSuite(TestSuite):

    def __init__(self):
        super().__init__()
        self.add_test_cases([TestVisualisation, TestLifeGameSimulation])
