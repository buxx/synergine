from synergine.src.core.connection.Display import Display as BaseDisplay
from synergine.src.core.SynergyObjectManager import SynergyObjectManager
from synergine.src.synergy.object.SynergyObject import SynergyObject
from synergine.src.core.display.DisplayZone import DisplayZone
from synergine.src.display.TwoDimensionalGrid import TwoDimensionalGrid


class Display(BaseDisplay):

    MOVE_DIRECTION_LEFT = (0, -1)
    MOVE_DIRECTION_UP = (-1, 0)
    MOVE_DIRECTION_RIGHT = (0, 1)
    MOVE_DIRECTION_DOWN = (1, 0)

    def __init__(self, config):
        super().__init__(config)
        self._zone = DisplayZone(20, 40)
        self._display_decal = (0, 0)
        self._grid = None

    def initialize(self):
        super().initialize()
        self._grid = TwoDimensionalGrid(self._get_config('display.grid.size', 1))

    def _object_displayable(self, obj: SynergyObject):
        # TODO: is inside en prennant en compte le zoom
        return self._zone.point_is_inside(obj.get_point())


    def receive(self, synergy_object_manager: SynergyObjectManager, context):
        for object_to_display in synergy_object_manager.get_objects_to_display():
            if self._object_displayable(object_to_display):
                self._draw_object_with_decal(object_to_display)

    def move_view_zone(self, direction):
        new_decal = (self._display_decal[0]+direction[0], self._display_decal[1]+direction[1])
        self._zone.move_zone(direction[0], direction[1])
        self._display_decal = new_decal

    def _update_zone_size(self, width, height):
        # TODO: Pk il faut inverser ? confusion qqpart
        self._zone.update_height(width-1)
        self._zone.update_width(height-2)

    def _draw_object_with_decal(self, obj: SynergyObject):
        object_point = self._grid.get_real_pixel_point(obj.get_point())
        adapted_point = (object_point[0]-self._display_decal[0]*self._grid.get_cell_size(),
                         object_point[1]-self._display_decal[1]*self._grid.get_cell_size())
        self.draw_object(obj, adapted_point)

    def draw_object(self, obj: SynergyObject, point):
        raise NotImplementedError

    def _get_real_screen_point(self, x, y, z=0):
        grid_point = self._grid.get_real_pixel_point((z, x, y))
        return (z, grid_point[0]-self._display_decal[0]*self._grid.get_cell_size(),
                   grid_point[1]-self._display_decal[1]*self._grid.get_cell_size())