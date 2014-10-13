import unittest
from synergine.src.test.TestSimulation import TestSimulation as BaseTestSimulation
from synergine.src.test.TestTerminal import TestTerminal
from tests.src.TestCollection import TestCollection
from tests.src.TestSimulation import TestSimulation as TestSimulationSimulation
from tests.src.TestCollectionConfiguration import TestCollectionConfiguration

class TestSimulation(BaseTestSimulation):

    def _get_set_up_simulation(self):
        return TestSimulationSimulation([TestCollection(TestCollectionConfiguration())])

    def test_cycles_in_main_process(self):
        self._test_cycles(True)

    def test_cycles_in_sub_process(self):
        self._test_cycles(False)

    def _test_cycles(self, main_process):
        tests = {
            0: [('john', 2, 2),
                    ('boby', 2, 5),
                    ('cora', 2, 10),
                    ('mara', 2, 20)],
            1: [('john', 4, 2),
                    ('boby', 32, 5),
                    ('cora', 1024, 10),
                    ('mara', 1048576, 20)],
            2: [('john', 16, 2),
                    ('boby', 0, 5),
                    ('cora', 0, 10),
                    ('mara', 0, 20)],
            3: [('john', 256, 2),
                    ('boby', 0, 5),
                    ('cora', 0, 10),
                    ('mara', 0, 20)],
            4: [('john', 65536, 2),
                    ('boby', 0, 5),
                    ('cora', 0, 10),
                    ('mara', 0, 20)],
            5: [],
        }
        for cycle in tests:
            synergy_object_manager = self._get_synergy_object_manager_for_cycle(cycles=cycle, main_process=main_process)
            self.assertEqual(sorted(tests[cycle]), sorted(self._get_objects_resume(synergy_object_manager)))

    def _get_objects_resume(self, synergy_object_manager):
        resume = []
        for obj in synergy_object_manager.get_objects():
            resume.append((obj.name, obj.beans, obj.coeff))
        return resume