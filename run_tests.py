from os import getcwd
from sys import path as ppath
ppath.insert(1,getcwd()+'/modules')

import unittest
from tests.TestSuite import TestSuite

runnable = unittest.TestSuite()
tests_suites = [TestSuite()]

for testsuite in tests_suites:
    for test_case in testsuite.get_test_cases():
        runnable.addTest(unittest.makeSuite(test_case))

runner=unittest.TextTestRunner()
test_result = runner.run(runnable)

if test_result.failures or test_result.errors:
  exit(1)

