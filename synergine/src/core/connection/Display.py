from synergine.src.core.connection.Terminal import Terminal
from synergine.src.core.SynergyObjectManager import SynergyObjectManager
from synergine.src.synergy.object.SynergyObject import SynergyObject
from synergine.src.core.display.ObjectVisualizer import ObjectVisualizer
from synergine.src.core.display.DisplayZone import DisplayZone


class Display(Terminal):
    """
    Graphical visualisation Terminal
    """
    MOVE_DIRECTION_LEFT = (0, -1)
    MOVE_DIRECTION_UP = (-1, 0)
    MOVE_DIRECTION_RIGHT = (0, 1)
    MOVE_DIRECTION_DOWN = (1, 0)

    def __init__(self, config={}):
        super().__init__(config)
        self._object_visualizer = ObjectVisualizer(config)
        self._zone = DisplayZone(20, 40)
        self._display_decal = (0, 0)

    def receive(self, synergy_object_manager: SynergyObjectManager):
        for object_to_display in synergy_object_manager.get_objects_to_display():
            if self._object_displayable(object_to_display):
                self.draw_object(object_to_display)

    def _object_displayable(self, obj: SynergyObject):
        return self._zone.object_is_inside(obj)
        # if self._zone.object_is_inside(obj):
        #     object_point = obj.get_point()
        #     width = self._zone.get_width()
        #     height = self._zone.get_height()
        #     if 0 <= object_point[1]+self._display_decal[0]:  # hauteur
        #         if 0 <= object_point[2]+self._display_decal[1]:  # largeur
        #             return True
        # return False

    def move_view_zone(self, direction):
        new_decal = (self._display_decal[0]+direction[0], self._display_decal[1]+direction[1])
        self._zone.move_zone(direction[0], direction[1])
        self._display_decal = new_decal

    def _update_zone_size(self, width, height):
        # TODO: Pk il faut inverser ? confusion qqpart
        self._zone.set_height(width-1)
        self._zone.set_width(height-2)

    def draw_object(self, obj: SynergyObject):
        raise NotImplementedError