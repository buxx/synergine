from pygame import image

from xyworld.display.object.ImageTraceVisualisation import ImageTraceVisualisation


class PygameImage(ImageTraceVisualisation):

    def __init__(self, value):
        super().__init__(value)
        self._surface = image.load(value)
        self._rectangle = self._surface.get_rect()

    def get_surface(self):
        return self._surface

    def get_rectangle(self):
        return self._rectangle
