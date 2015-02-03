from os import getcwd
from sys import path as ppath
ppath.insert(1,getcwd()+'/vendor') # TODO: win32 compatibilite (python path)

import unittest
from lifegame.test.LifeGameTestSuite import LifeGameTestSuite
from tests.TestSuite import TestSuite

# TODO: Lister les tests ailleurs ? Recuperer les suite de tests de module auto
# (rappel: avant on utilise config.config mais il y avait un import croise)

runnable = unittest.TestSuite()
tests_suites = [TestSuite(), LifeGameTestSuite()]

for testsuite in tests_suites:
    for test_case in testsuite.get_test_cases():
        runnable.addTest(unittest.makeSuite(test_case))

runner=unittest.TextTestRunner()
runner.run(runnable)