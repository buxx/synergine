from synergine.src.core.connection.Terminal import Terminal

class TestTerminal(Terminal):

    def __init__(self):
        self._synergy_object_manager = None

    def receive(self, synergy_object_manager):
        self._synergy_object_manager = synergy_object_manager

    def get_synergy_object_manager(self):
        return self._synergy_object_manager