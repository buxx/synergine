from synergine.core.cycle.Context import Context as BaseContext
from xyzworld.cst import *


class Context(BaseContext):

    def get_objects_ids_near_point(self, point, distance=1): # TODO distance
        objects_ids_arrounds = []
        for point_arround in self.get_arround_points_of_point(point):
            point_objects_ids = self.metas.list.get(POSITIONS, point_arround, allow_empty=True)
            for object_id in point_objects_ids:
                objects_ids_arrounds.append(object_id)
        return objects_ids_arrounds

    def get_objects_ids_by_position_near_point(self, point, distance=1): # TODO distance
        objects_ids_arrounds_by_point = {}
        for point_arround in self.get_arround_points_of_point(point):
            objects_ids_arrounds_by_point[point_arround] = []
            point_objects_ids = self.metas.list.get(POSITIONS, point_arround, allow_empty=True)
            for object_id in point_objects_ids:
                objects_ids_arrounds_by_point[point_arround].append(object_id)
        return objects_ids_arrounds_by_point

    # TODO: Ces methodes de points devrait etre ailleurs
    def get_arround_points_of(self, point, distance):
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
        return points

    def get_arround_points_of_point(self, point):
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

