from synergine.src.core.connection.Display import Display
import pygame


class PygameDisplay(Display):

    _name = "pygame"

    def __init__(self, config):
        super().__init__(config)
        self._screen = None
        self._screen_size = (0, 0)
        self._event = None
        self._default_font = None

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
        background.fill((0, 0, 0))
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
                    self.move_view_zone(Display.MOVE_DIRECTION_UP)
                elif event.key == pygame.K_RIGHT:
                    self.move_view_zone(Display.MOVE_DIRECTION_DOWN)
                elif event.key == pygame.K_UP:
                    self.move_view_zone(Display.MOVE_DIRECTION_LEFT)
                elif event.key == pygame.K_DOWN:
                    self.move_view_zone(Display.MOVE_DIRECTION_RIGHT)
                elif event.key == pygame.K_a:
                    self._grid.set_cell_size(self._grid.get_cell_size()-5)
                elif event.key == pygame.K_z:
                    self._grid.set_cell_size(self._grid.get_cell_size()+5)



    def terminate(self):
        pass

    def _update_screen_size(self):
        self._screen_size = self._screen.get_size()
        self._update_zone_size(self._screen_size[0], self._screen_size[1])

    def draw_object(self, obj, point):
        obj_visual = self._object_visualizer.get_visual(obj)
        visual_surface = obj_visual.get_surface()
        visual_size = visual_surface.get_size()
        visual_surface = pygame.transform.scale(visual_surface, (round(visual_size[0]*self._grid.get_ratio()),
                                                                 round(visual_size[1]*self._grid.get_ratio())))
        self._screen.blit(visual_surface, point)
