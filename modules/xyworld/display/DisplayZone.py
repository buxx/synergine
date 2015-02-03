class DisplayZone():

    def __init__(self, width, height):
        # TODO: Width et Height auto en fonction de la taille de la fenetre
        self._width = width
        self._height = height
        self._zone_start = (0, 0, 0)
        self._zone_end = (0, width, height)

    def get_width(self):
        return self._width

    def update_width(self, new_width):
        new_position = self._zone_start[2]+new_width
        self._zone_end = (0, self._zone_end[1], new_position)
        self._width = new_width

    def get_height(self):
        return self._height

    def update_height(self, new_height):
        new_position = self._zone_start[1]+new_height
        self._zone_end = (0, new_position, self._zone_end[2])
        self._height = new_height

    def get_zone_start(self):
        return self._zone_start

    def get_zone_end(self):
        return self._zone_end

    def move_zone(self, x, y, z = 0):
        self._zone_start = (z, self._zone_start[1]+y, self._zone_start[2]+x)
        self._zone_end = (z, self._zone_end[1]+y, self._zone_end[2]+x)

    def point_is_inside(self, point):
        # (0, 42, 0)
        # ((0, 0, 0), (0, 158, 42))
        if self._zone_end[0] >= point[0] >= self._zone_start[0]:
            if self._zone_end[1] >= point[2] >= self._zone_start[1]:
                if self._zone_end[2] >= point[1] >= self._zone_start[2]:
                    return True
        return False