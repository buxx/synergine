from xyworld.display.Display import Display as XyDisplay
import pygame


class PygameDisplay(XyDisplay):

    _name = "pygame"

    def __init__(self, config, context):
        super().__init__(config, context)
        self._screen = None
        self._screen_size = (0, 0)
        self._event = None
        self._default_font = None
        self._visuals_surface_cache = {}

    def initialize(self):
        super().initialize()
        pygame.init()
        self._screen = pygame.display.set_mode(self._get_config('window_size'))
        pygame.display.set_caption(self._get_config('app.name'))
        self._screen_size = self._screen.get_size()
        self._event = pygame.event
        self._default_font = pygame.font.SysFont(self._get_config('font.name'), self._get_config('font.size'))
        self._update_screen_size()

    def initialize_screen(self, screen):
        pass

    def start_of_cycle(self):
        screen_size = self._screen.get_size()
        if screen_size != self._screen_size:
            self._update_screen_size()
        background = pygame.Surface(self._screen_size)
        background = background.convert()
        background.fill(self._get_config('background.color'))
        self._screen.blit(background, (0, 0))

    def end_of_cycle(self):

        ## Debug traces
        # label = self._default_font.render('size '+str((self._zone.get_width(), self._zone.get_height())), 1, (255,255,0))
        # self._screen.blit(label, (0, 0))
        #
        # label = self._default_font.render('decal '+str(self._display_decal), 1, (255,255,0))
        # self._screen.blit(label, (0, 15))
        #
        # label = self._default_font.render('zone_start '+str(self._zone.get_zone_start()), 1, (255,255,0))
        # self._screen.blit(label, (0, 30))
        #
        # label = self._default_font.render('zone_end '+str(self._zone.get_zone_end()), 1, (255,255,0))
        # self._screen.blit(label, (0, 45))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_view_zone(self._get_decal_with_zoom(XyDisplay.MOVE_DIRECTION_UP))
                elif event.key == pygame.K_RIGHT:
                    self.move_view_zone(self._get_decal_with_zoom(XyDisplay.MOVE_DIRECTION_DOWN))
                elif event.key == pygame.K_UP:
                    self.move_view_zone(self._get_decal_with_zoom(XyDisplay.MOVE_DIRECTION_LEFT))
                elif event.key == pygame.K_DOWN:
                    self.move_view_zone(self._get_decal_with_zoom(XyDisplay.MOVE_DIRECTION_RIGHT))
                elif event.key == pygame.K_a:
                    if self._grid.get_cell_size()-5 > 0:
                      self._grid.set_cell_size(self._grid.get_cell_size()-5)
                      self._set_zoom(self.get_zoom()+20)
                elif event.key == pygame.K_z:
                    self._grid.set_cell_size(self._grid.get_cell_size()+5)
                    self._set_zoom(self.get_zoom()-20)
                else:
                    self._key_pressed(event.key)

    def _key_pressed(self, key):
        pass

    def _get_decal_with_zoom(self, decal):
        return (decal[0] * self.get_zoom(), decal[1] * self.get_zoom())

    def terminate(self):
        pass

    def _update_screen_size(self):
        self._screen_size = self._screen.get_size()
        self._update_zone_size(self._screen_size[0], self._screen_size[1])

    def draw_objects(self, objects, point):
        obj_visual, concerneds_objects = self._object_visualizer.get_for_position(point, objects)
        if obj_visual:
            visual_surface = self._get_visual_surface(obj_visual)
            self._screen.blit(visual_surface, point)
        for obj in objects:
            if concerneds_objects is [] or obj not in concerneds_objects:
                self.draw_object(obj, point)

    def draw_object(self, obj, point):
        obj_visual = self._object_visualizer.get_visual(obj)
        visual_surface = self._get_visual_surface(obj_visual)
        self._screen.blit(visual_surface, point)

    def _get_visual_surface(self, obj_visual):
        ratio = self._grid.get_ratio()
        if obj_visual in self._visuals_surface_cache:
            if ratio in self._visuals_surface_cache[obj_visual]:
                return self._visuals_surface_cache[obj_visual][ratio]

        visual_surface = obj_visual.get_surface()
        visual_size = visual_surface.get_size()
        visual_surface_for_ratio = pygame.transform.scale(visual_surface, (round(visual_size[0]*ratio),
                                                                           round(visual_size[1]*ratio)))
        self._visuals_surface_cache[obj_visual] = {}
        self._visuals_surface_cache[obj_visual][ratio] = visual_surface_for_ratio
        return visual_surface_for_ratio