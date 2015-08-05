from synergine.test.TestSimulation import TestSimulation as BaseTestSimulation
from tests.src.TestCollection import TestCollection
from tests.src.TestSimulation import TestSimulation as TestSimulationSimulation
from tests.src.TestCollectionConfiguration import TestCollectionConfiguration


class TestCycleCallback(BaseTestSimulation):

    _callback_call_count = -1

    def _get_set_up_simulations(self):
        return [TestSimulationSimulation([TestCollection(TestCollectionConfiguration())])]

    def test_cycles_callbacks(self):
        self._connection.receive_callback = self._cycle_callback

        self._callback_call_count = -1
        core = self.get_core(5)
        core.run()

        self.assertEquals(5, self._callback_call_count)

    def _cycle_callback(self, terminal, actions_done):
        self._callback_call_count += 1
        self.assertEquals(self._callback_call_count, terminal.get_context().get_cycle())
