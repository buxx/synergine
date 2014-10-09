class Context():

    def __init__(self, synergy_object_manager):
        self._synergy_object_manager = synergy_object_manager
        self._map = {}

    def get_collections(self):
        # TODO: C'est son job ?
        return self._synergy_object_manager.get_collections()

    def get_simulations(self):
        # TODO: C'est son job ?
        return self._synergy_object_manager.get_simulations()

    def get_objects(self):
        # TODO: C'est son job ?
        return self._synergy_object_manager.get_objects()

    def update(self):
        self._update_map()

    def _update_map(self):
        # TODO: Calculer les nouveautes de la map seulement ? pour eco des ressources
        # Les objets qui n'ont pas bouge n'ont pas besoin d'etre recalcule (self._synergy_object_manager.get_objects_to_display())
        # il faut cependant trouver un moyen performant de savoir qui est a faire disparaitre (avant de redessiner)
        self._map = {}
        for object in self._synergy_object_manager.get_objects():
            for point in object.get_trace():
                if point in self._map:
                    self._map[point].append(object)
                else:
                    self._map[point] = [object]

    def get_map(self):
        return self._map

    def get_objects_near_point(self, point, distance=1): # TODO distance
        # TODO: Ces fonctions sont-elles de la responsabilite de Context ?
        objects_arrounds = []
        for point_arround in self.get_arround_points_of_point(point):
            if point_arround in self._map:
                for obj in self._map[point_arround]:
                    objects_arrounds.append(obj)
        return objects_arrounds

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