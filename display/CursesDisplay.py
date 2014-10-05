from src.core.connection.Display import Display
import curses

class CursesDisplay(Display):
  # TODO: gestion de ce qui est affiche, partie de la map totale

  def __init__(self):
    super(CursesDisplay, self).__init__()
    self._screen = None

  def needToRunCore(self):
    return True
  
  def encapsulate_run(self, run_function):
    super(CursesDisplay, self).encapsulate_run(run_function)
    curses.wrapper(run_function)
  
  def initializeScreen(self, screen):
    self._screen = screen
    curses.noecho()
    curses.cbreak()
    self._screen.keypad(True)
  
  def _startOfCycle(self):
    self._screen.clear()
  
  def _endOfCycle(self):
    self._screen.refresh()
  
  def terminate(self):
    curses.nocbreak()
    self._screen.keypad(False)
    curses.echo()
    curses.endwin()
    self._screen = None
  
  def drawPoints(self, points):
    for point in points:
      # todo: z ... au moins valeur par defaut (generique !)
      if point == (0,23,20): # TEST
        self._screen.addstr(point[1], point[2], "*")
      else:
        self._screen.addstr(point[1], point[2], "*")