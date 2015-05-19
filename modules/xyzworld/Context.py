from synergine.core.cycle.Context import Context as BaseContext
from xyzworld.cst import *


class Context(BaseContext):
    """

    Context override offering 2D and 3D metas data exploitation methods.

    """

    def get_objects_ids_near_point(self, point, distance=1):  # TODO distance
        """

        Return objects ids positioned around a point.

        :param point: (z, x, y) tuple
        :param distance: ! not used at the moment
        :return: list of ``SynergyObject`` ids
        :rtype: list
        """
        objects_ids_arounds = []
        for point_around in self.get_around_points_of_point(point):
            point_objects_ids = self.metas.list.get(POSITIONS, point_around, allow_empty=True)
            for object_id in point_objects_ids:
                objects_ids_arounds.append(object_id)
        return objects_ids_arounds

    def get_objects_ids_by_position_near_point(self, point, distance=1): # TODO distance
        """

        Return objects ids positioned around a point, ordered by positions.

        :param point: (z, x, y) tuple
        :param distance: ! not used at the moment
        :return: dict with by position key: list of ``SynergyObject`` ids
        """
        objects_ids_arounds_by_point = {}
        for point_around in self.get_around_points_of_point(point):
            objects_ids_arounds_by_point[point_around] = []
            point_objects_ids = self.metas.list.get(POSITIONS, point_around, allow_empty=True)
            for object_id in point_objects_ids:
                objects_ids_arounds_by_point[point_around].append(object_id)
        return objects_ids_arounds_by_point

    # TODO: Ces methodes de points devrait etre ailleurs
    def get_around_points_of(self, point, distance=1):
        """

        Return positions around a point.

        :param point: (z, x, y) tuple
        :param distance: Distance to compute
        :return: list of (z, x, y) positions
        :rtype: list
        """
        start_x = point[1] - distance
        start_y = point[2] - distance
        #start_z = point[0] - distance
        points = []
        range_distance = (distance*2)+1
        for dx in range(range_distance):
            for dy in range(range_distance):
                #for dz in range(range_distance):
                    #points.append((start_z+dz, start_x+dx, start_y+dy))
                points.append((0, start_x+dx, start_y+dy))
        points.remove(point)
        return points

    def get_around_points_of_point(self, point):
        """

        Return positions around a point with distance of 1.

        :param point: (z, x, y) tuple
        :return: list of (z, x, y) positions
        :rtype: list
        """
        pos = point
        pz = pos[0]
        px = pos[1]
        py = pos[2]
        return (
            (pz, px-1, py-1),
            (pz, px,     py-1),
            (pz, px+1, py+1),
            (pz, px-1, py    ),
            (pz, px+1, py    ),
            (pz, px-1, py+1),
            (pz, px,     py+1),
            (pz, px+1, py-1)
        )

