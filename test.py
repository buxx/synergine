import unittest
from src.core.config.ConfigurationManager import ConfigurationManager
from config import config

configuration_manager = ConfigurationManager(config)
runnable = unittest.TestSuite()

for testsuite in configuration_manager.get('test.suites'):
  for test_case in testsuite.getTestCases():
    runnable.addTest(unittest.makeSuite(test_case))

runner=unittest.TextTestRunner()
runner.run(runnable)