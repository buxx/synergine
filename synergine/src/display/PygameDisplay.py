from synergine.src.core.connection.Display import Display
import pygame


class PygameDisplay(Display):

    def __init__(self, config={}):
        super().__init__(config)
        self._screen = None
        self._screen_size = (0, 0)
        # TODO: > ._xx
        pygame.init()
        self._screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Fooooooooooo')
        self._screen_size = self._screen.get_size()

        self.event = pygame.event
        self.default_font = pygame.font.SysFont("arial", 11)

    def initialize(self):
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
        pygame.display.update()

    def terminate(self):
        pass

    def _update_screen_size(self):
        self._screen_size = self._screen.get_size()
        self._update_zone_size(self._screen_size[0], self._screen_size[1])

    def draw_object(self, obj):

        point = obj.get_point()
        obj_visual = self._object_visualizer.get_visual(obj)
        visual_surface = obj_visual.get_surface()
        # TODO: Gestionnaire de grille
        self._screen.blit(visual_surface, (point[1]*20, point[2]*20))
