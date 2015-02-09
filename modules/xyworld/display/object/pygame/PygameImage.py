from pygame import image

from xyworld.display.object.ImageTraceVisualisation import ImageTraceVisualisation


class PygameImage(ImageTraceVisualisation):

    @classmethod
    def from_filepath(cls, filepath):
      surface = image.load(filepath)
      return cls(surface)

    def __init__(self, surface):
        self._surface = surface
        self._rectangle = self._surface.get_rect()

    def get_surface(self):
        return self._surface

    def get_rectangle(self):
        return self._rectangle
