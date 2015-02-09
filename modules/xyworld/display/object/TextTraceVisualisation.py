from xyworld.display.object.Visualisation import Visualisation


class TextTraceVisualisation(Visualisation):

    # TODO: not LISKOV
    def __init__(self, value):
        self._value = value

    def get_char(self):
        return self._value