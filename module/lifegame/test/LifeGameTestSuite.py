from synergine.src.test.TestSuite import TestSuite
from module.lifegame.test.simulation.TestLifeGameSimulation import TestLifeGameSimulation

class LifeGameTestSuite(TestSuite):

    def __init__(self):
        super().__init__()
        self.add_test_cases([TestLifeGameSimulation])
