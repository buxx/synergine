from synergine.src.synergy.object.SynergyObject import SynergyObject


class DisplayZone():

    def __init__(self, width, height):
        # TODO: Width et Height auto en fonction de la taille de la fenetre
        self._width = width
        self._height = height
        self._zone_start = (0, 0, 0)
        self._zone_end = (0, width, height)

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._zone_end = (0, self._zone_end[1], width)
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._zone_end = (0, height, self._zone_end[2])
        self._height = height

    def get_zone_start(self):
        return self._zone_start

    def get_zone_end(self):
        return self._zone_end

    def move_zone(self, x, y, z = 0):
        self._zone_start = (z, self._zone_start[1]+y, self._zone_start[2]+x)
        self._zone_end = (z, self._zone_end[1]+y, self._zone_end[2]+x)

    def object_is_inside(self, obj: SynergyObject):
        # (0, 42, 0)
        # ((0, 0, 0), (0, 158, 42))
        object_point = obj.get_point()
        if self._zone_end[0] >= object_point[0] >= self._zone_start[0]:
            if self._zone_end[1] >= object_point[2] >= self._zone_start[1]:
                if self._zone_end[2] >= object_point[1] >= self._zone_start[2]:
                    return True
        return False