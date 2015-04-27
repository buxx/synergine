from synergine.core.connection.Terminal import Terminal


class TestTerminal(Terminal):
    _name = 'tests_test'

    def __init__(self, config, context):
        super().__init__(config, context)
        self._synergy_object_manager = None

    # TODO: inutile non ?
    def receive(self, synergy_object_manager, context):
        self._synergy_object_manager = synergy_object_manager

    def get_synergy_object_manager(self):
        return self._synergy_object_manager