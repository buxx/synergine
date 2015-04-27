from synergine.core.connection.Terminal import Terminal


class TestTerminal(Terminal):
    _name = 'tests_test'

    def __init__(self, config, context, synergy_manager):
        super().__init__(config, context, synergy_manager)

    # TODO: inutile non ?
    def receive(self, actions_done):
        pass

    def get_synergy_object_manager(self):
        return self._synergy_manager