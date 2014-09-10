from src.core.display.Display import Display
import curses

class CursesDisplay(Display):
  # TODO: gestion de ce qui est affiche, partie de la map totale
  
  def needToRunDisplay(self):
    return True
  
  def encapsulate_run(self, run_function):
    curses.wrapper(run_function)
  
  def __init__(self):
    super(CursesDisplay, self).__init__()
    self._screen = None
  
  def initializeScreen(self, screen):
    self._screen = screen
    curses.noecho()
    curses.cbreak()
    self._screen.keypad(True)
  
  def endOfCycle(self):
    self._screen.refresh()
  
  def terminate(self):
    curses.nocbreak()
    self._screen.keypad(False)
    curses.echo()
    curses.endwin()
  
  def drawPoints(self, points):
    for point in points:
      # todo: z ... au moins valeur par defaut (generique !)
      self._screen.addstr(point[1], point[2], "*")