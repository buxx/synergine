class TestSuite:

    def __init__(self):
        self._test_cases = []

    def add_test_cases(self, test_cases):
        for test_case in test_cases:
            self._test_cases.append(test_case)

    def get_test_cases(self):
        return self._test_cases