from synergine.core.connection.Display import Display as BaseDisplay
from synergine.core.SynergyObjectManager import SynergyObjectManager
from synergine.synergy.object.SynergyObject import SynergyObject
from xyworld.display.DisplayZone import DisplayZone
from synergine.display.TwoDimensionalGrid import TwoDimensionalGrid
# TODO: POSITIONS doit devdenir xyworld (pas z)
from xyzworld.cst import POSITIONS

class Display(BaseDisplay):

    MOVE_DIRECTION_LEFT = (0, -1)
    MOVE_DIRECTION_UP = (-1, 0)
    MOVE_DIRECTION_RIGHT = (0, 1)
    MOVE_DIRECTION_DOWN = (1, 0)

    def __init__(self, config, context):
        super().__init__(config, context)
        self._zone = DisplayZone(20, 40)
        self._display_decal = (0, 0)
        self._grid = None
        self._zoom = 1

    def initialize(self):
        super().initialize()
        self._grid = TwoDimensionalGrid(self._get_config('display.grid.size', 1))

    def _position_displayable(self, position):
        # TODO: is inside en prennant en compte le zoom
        return self._zone.point_is_inside(position)


    def receive(self, synergy_object_manager: SynergyObjectManager, context):
        # Idee: recevoir les objets organises par positions (POSITIONS)
        """
        a: pour chaque position, si position displayable, draw les objets de la position
        b: dessiner pour les objets de la position (on se fait retourner les obj dessiner)
           on dessine un a un les obj non dessine
        """
        # for object_to_display in synergy_object_manager.get_objects_to_display():
        #     if self._object_displayable(object_to_display):
        #         self._draw_object_with_decal(object_to_display)
        positions = context.metas.list.get_collection(POSITIONS)
        for position in positions:
            if self._position_displayable(position):
                objects_in_position = [synergy_object_manager.get_map().get_object(obj_id) \
                                       for obj_id in positions[position]]
                self._draw_objects_with_decal(position, objects_in_position)

    def move_view_zone(self, direction):
        new_decal = (self._display_decal[0]+direction[0], self._display_decal[1]+direction[1])
        self._zone.move_zone(direction[0], direction[1])
        self._display_decal = new_decal

    def _update_zone_size(self, width, height):
        # TODO: Pk il faut inverser ? confusion qqpart
        self._zone.update_height(width-1)
        self._zone.update_width(height-2)

    def _draw_objects_with_decal(self, position, objects):
        pixel_point = self._grid.get_real_pixel_point(position)
        adapted_point = (pixel_point[0]-self._display_decal[0]*self._grid.get_cell_size(),
                         pixel_point[1]-self._display_decal[1]*self._grid.get_cell_size())
        self.draw_objects(objects, adapted_point)

    def draw_objects(self, objects, point):
        raise NotImplementedError

    def _get_real_screen_point(self, x, y, z=0):
        grid_point = self._grid.get_real_pixel_point((z, x, y))
        return (z, grid_point[0]-self._display_decal[0]*self._grid.get_cell_size(),
                   grid_point[1]-self._display_decal[1]*self._grid.get_cell_size())

    def get_zoom(self):
        return self._zoom

    def _set_zoom(self, zoom):
        self._zoom = zoom