from synergine.src.core.connection.Display import Display
import curses


class CursesDisplay(Display):
    # TODO: gestion de ce qui est affiche, partie de la map totale

    def __init__(self, config={}):
        super().__init__(config)
        self._screen = None

    def need_to_run_core(self):
        return True

    def encapsulate_run(self, run_function):
        super().encapsulate_run(run_function)
        curses.wrapper(run_function)

    def initialize_screen(self, screen):
        self._screen = screen
        curses.noecho()
        curses.cbreak()
        self._screen.keypad(True)

    def _start_of_cycle(self):
        self._screen.clear()

    def _end_of_cycle(self):
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
        self._screen.addstr(point[1], point[2], self._get_object_char(obj))