from src.core.connection.Terminal import Terminal
from src.core.SynergyObjectManager import SynergyObjectManager

class Display(Terminal):
    """
    Graphical visualisation Terminal
    """

    def receive(self, synergy_object_manager):
        self._start_of_cycle()
        for object_to_display in synergy_object_manager.get_objects_to_display():
            # TODO: drawObject() avec un objet generique affichable par un Display
            self.draw_points(object_to_display.get_trace())
        self._end_of_cycle()

    def _start_of_cycle(self):
        raise NotImplementedError

    def _end_of_cycle(self):
        raise NotImplementedError

    def draw_points(self, points):
        raise NotImplementedError