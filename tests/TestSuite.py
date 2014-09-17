from src.test.TestSuite import TestSuite as BaseTestSuite
from tests.simulation.TestSimulation import TestSimulation

class TestSuite(BaseTestSuite):
  
  def __init__(self):
    super(TestSuite, self).__init__()
    self.addTestCases([TestSimulation])
