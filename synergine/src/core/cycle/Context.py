#from synergine.src.core.Core import Core
# TODO: La notion de position appartient a LifeGame (ou a un addon)
from module.lifegame.synergy.LifeGameSimulation import LifeGameSimulation
from synergine.metas import metas


class Context():
    """
    This object contain a representation of simulation. It's
    used by Action to know what exist in the synergy simulation
    """

    def __init__(self):
        #self._synergy_object_manager = synergy_object_manager
        #self._map = {}
        self.metas = metas

    # TODO opt/fullint: ca devient des points !
    # TODO: Ca devrai etre dependant de lifesimulation (notion de positions)
    def get_objects_ids_near_point(self, point, distance=1): # TODO distance
        # TODO: Ces fonctions sont-elles de la responsabilite de Context ?
        objects_ids_arrounds = []
        for point_arround in self.get_arround_points_of_point(point):
            point_objects_ids = self.metas.list.get(LifeGameSimulation.POSITIONS, point_arround)
            for object_id in point_objects_ids:
                objects_ids_arrounds.append(object_id)
        return objects_ids_arrounds

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