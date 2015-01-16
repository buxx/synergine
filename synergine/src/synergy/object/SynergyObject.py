from synergine.src.synergy.object.SynergyObjectInterface import SynergyObjectInterface


class SynergyObject(SynergyObjectInterface):

    SIGNAL_CREATED = 'object.created'
    SIGNAL_DELETED = 'object.deleted'

    def __init__(self):
        self._cycle_frequency = 1
        # TODO: Cet histoire de trace est trop dependante d'objet a trace
        self._trace_length = 1
        self._trace = []
        self._id = id(self)

    def get_id(self):
        return self._id

    # TODO: Gestion space dtata autrement ?
    def add_trace(self, point):
        # TODO: limite de taille de trace
        self._trace.append(point)

    def get_trace(self):
        return self._trace

    def get_point(self):
        """
        Return the last insered trace point
        :return: (z, x, y)
        """
        trace = self.get_trace()
        return trace[len(trace)-1]

    def end_cycle(self):
        pass