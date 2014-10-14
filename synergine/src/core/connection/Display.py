from synergine.src.core.connection.Terminal import Terminal
from synergine.src.core.SynergyObjectManager import SynergyObjectManager
from synergine.src.synergy.object.SynergyObject import SynergyObject
from synergine.src.core.display.ObjectVisualizer import ObjectVisualizer

class Display(Terminal):
    """
    Graphical visualisation Terminal
    """

    def __init__(self, config={}):
        super().__init__(config)
        self._object_visualizer = ObjectVisualizer(config)

    def receive(self, synergy_object_manager: SynergyObjectManager):
        self._start_of_cycle()
        for object_to_display in synergy_object_manager.get_objects_to_display():
            # TODO: drawObject() avec un objet generique affichable par un Display
            self.draw_object(object_to_display)
        self._end_of_cycle()

    def _start_of_cycle(self):
        raise NotImplementedError

    def _end_of_cycle(self):
        raise NotImplementedError

    def draw_object(self, obj: SynergyObject):
        raise NotImplementedError