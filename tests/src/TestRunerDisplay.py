from synergine.test.TestDisplay import TestDisplay

class TestRunerDisplay(TestDisplay):

    _name = 'test_runner'

    def need_to_run_core(self):
        return True