class Signal:

    def __init__(self):
        self._listeners = []

    def connect(self, callback):
        self._listeners.append(callback)

    def send(self, **kwargs):
        for listener in self._listeners:
            listener(**kwargs)