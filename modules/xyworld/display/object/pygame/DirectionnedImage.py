from xyworld.display.object.pygame.PygameImage import PygameImage
from pygame.transform import rotate


class DirectionnedImage():

    def __init__(self, image: PygameImage):
        self._image = image
        self._directions_images = {}
        self._update_directions_images()

    def _update_directions_images(self):
      image_surface = self._image.get_surface()
      self._directions_images[10] = PygameImage(rotate(image_surface, 45))
      self._directions_images[11] = self._image
      self._directions_images[12] = PygameImage(rotate(image_surface, -45))
      self._directions_images[13] = PygameImage(rotate(image_surface, 90))
      self._directions_images[14] = self._image
      self._directions_images[15] = PygameImage(rotate(image_surface, -90))
      self._directions_images[16] = PygameImage(rotate(image_surface, 135))
      self._directions_images[17] = PygameImage(rotate(image_surface, 180))
      self._directions_images[18] = PygameImage(rotate(image_surface, -135))

    def get_for_direction(self, direction):
      return self._directions_images[direction]
