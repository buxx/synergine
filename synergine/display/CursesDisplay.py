from synergine.src.core.connection.Display import Display
from synergine.src.synergy.object.SynergyObject import SynergyObject
import curses


class CursesDisplay(Display):

    def __init__(self, config={}):
        super().__init__(config)
        self._screen = None

    def need_to_run_core(self):
        return True

    def encapsulate_run(self, run_function):
        super().encapsulate_run(run_function)
        curses.wrapper(run_function)

    def initialize(self):
        screen_size = self._screen.getmaxyx()
        self._update_zone_size(screen_size[1], screen_size[0])

    def initialize_screen(self, screen):
        self._screen = screen
        curses.noecho()
        curses.cbreak()
        self._screen.keypad(True)
        self._screen.nodelay(True)

    def start_of_cycle(self):
        self._screen.clear()

    def end_of_cycle(self):
        self._draw_components()

        pressed_key = self._screen.getch()
        if pressed_key == curses.KEY_LEFT:
            self.move_view_zone(Display.MOVE_DIRECTION_LEFT)
        if pressed_key == curses.KEY_UP:
            self.move_view_zone(Display.MOVE_DIRECTION_UP)
        if pressed_key == curses.KEY_RIGHT:
            self.move_view_zone(Display.MOVE_DIRECTION_RIGHT)
        if pressed_key == curses.KEY_DOWN:
            self.move_view_zone(Display.MOVE_DIRECTION_DOWN)
        self._screen.refresh()

    def terminate(self):
        curses.nocbreak()
        self._screen.keypad(False)
        curses.echo()
        curses.endwin()
        self._screen = None

    def _get_object_char(self, obj):
        return self._object_visualizer.get_visual(obj).get_char()

    def draw_object(self, obj):
        point = obj.get_point()
        self._screen.addstr(point[1]-self._display_decal[0], point[2]-self._display_decal[1], self._get_object_char(obj))

    def _draw_components(self):
        self._draw_view_zone_border()

    def _draw_view_zone_border(self):
        width = self._zone.get_width()
        height = self._zone.get_height()
        for x in range(0, width):
            self._screen.addstr(x+1, 0, '|')
            self._screen.addstr(x+1, height, '|')
        for y in range(0, height):
            self._screen.addstr(0, y+1, '-')
            self._screen.addstr(width, y+1, '-')
        self._screen.addstr(0, 0, '+')
        self._screen.addstr(0, height, '+')
        self._screen.addstr(width, 0, '+')
        self._screen.addstr(width, height, '+')