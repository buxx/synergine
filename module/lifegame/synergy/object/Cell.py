from synergine.src.synergy.object.SynergyObject import SynergyObject

class Cell(SynergyObject):

    def __init__(self):
        super().__init__()
        self._alive = False

    def add_trace(self, point):
        """
        Cell have only one point length
        """
        self._trace = [point]

    def set_point(self, point):
        self.add_trace(point)

    def get_point(self):
        return self.get_trace()[0]

    def set_alive(self, alive):
        self._alive = alive

    def is_alive(self):
        return self._alive