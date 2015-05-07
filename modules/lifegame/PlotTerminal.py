from synergine.core.connection.Terminal import Terminal
import matplotlib.pyplot as plt


class PlotTerminal(Terminal):
    """
    A very simple Terminal to see how many cells are alive in plot.
    """

    def __init__(self, config, context, synergy_manager):
        super().__init__(config, context, synergy_manager)
        plt.axis([0, 1, 0, 1])
        plt.ion()
        plt.show()
        self._max_alive = 0

    def receive(self, actions_done):
        objects = self._synergy_manager.get_objects()
        alive_objects = [obj for obj in objects if obj.is_alive()]
        cycle = self._context.get_cycle()

        y = len(alive_objects)

        if y > self._max_alive:
            self._max_alive = y

        plt.axis([0, cycle, 0, self._max_alive])
        plt.scatter(cycle, y)
        plt.draw()
