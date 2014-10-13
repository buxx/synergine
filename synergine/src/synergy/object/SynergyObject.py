from synergine.src.synergy.object.SynergyObjectInterface import SynergyObjectInterface

class SynergyObject(SynergyObjectInterface):

    def __init__(self):
        self._cycle_frequency = 1
        # TODO: Cet histoire de trace est trop dependante d'objet a trace
        self._trace_length = 1
        self._trace = []
        self._will = None

    def set_will(self, action):
        self._will = action

    def get_will(self):
        return self._will

    # TODO: Gestion space dtata autrement ?
    def add_trace(self, point):
        # TODO: limite de taille de trace
        self._trace.append(point)

    def get_trace(self):
        return self._trace
