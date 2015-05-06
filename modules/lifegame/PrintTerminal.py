from synergine.core.connection.Terminal import Terminal


class PrintTerminal(Terminal):
    """
    A very simple Terminal to see how many cells are alive and dead.
    """

    def receive(self, actions_done):
        objects = self._synergy_manager.get_objects()
        alive_objects = [obj for obj in objects if obj.is_alive()]
        died_objects = [obj for obj in objects if not obj.is_alive()]
        cycle = self._context.get_cycle()

        print("Cycle %d: %d cells alive, %d cells died." % (cycle, len(alive_objects), len(died_objects)))