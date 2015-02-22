from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from xyzworld.cst import *


class Cell(XyzSynergyObject):

    def __init__(self, context):
        super().__init__(context)
        self._alive = False
        self._alive_since = 0
        self._died_since = 0
        self.test = 0

    def set_alive(self, alive):
        self._alive_since = -1
        self._died_since = -1
        self._alive = alive

    def is_alive(self):
        return self._alive

    def get_is_alive_since(self):
        return self._alive_since

    def get_is_died_since(self):
        return self._died_since

    def end_cycle(self):
        if self.is_alive():
            self._alive_since += 1
        else:
            self._died_since += 1