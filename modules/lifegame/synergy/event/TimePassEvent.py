from synergine.synergy.event.Event import Event


class TimePassEvent(Event):

    def _prepare(self, obj, context, parameters={}):
        # All cells are concerned
        return parameters
