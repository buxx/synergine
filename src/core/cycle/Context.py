class Context(object):
  
  def __init__(self, synergy_object_manager):
    self._synergy_object_manager = synergy_object_manager
    self._map = {}

  def getCollections(self):
    # TODO: C'est son job ?
    return self._synergy_object_manager.getCollections()

  def getSimulations(self):
    # TODO: C'est son job ?
    return self._synergy_object_manager.getSimulations()

  def getObjects(self):
    # TODO: C'est son job ?
    return self._synergy_object_manager.getObjects()

  def update(self):
    self._updateMap()
  
  def _updateMap(self):
    # TODO: Calculer les nouveautes de la map seulement ? pour eco des ressources
    # Les objets qui n'ont pas bouge n'ont pas besoin d'etre recalcule (self._synergy_object_manager.getObjectsToDisplay())
    # il faut cependant trouver un moyen performant de savoir qui est a faire disparaitre (avant de redessiner)
    self._map = {}
    for object in self._synergy_object_manager.getObjects():
      for point in object.getTrace():
        if point in self._map:
          self._map[point].append(object)
        else:
          self._map[point] = [object]
  
  def getMap(self):
    return self._map

  def getObjectsNearPoint(self, point, distance=1): # TODO distance
    # TODO: Ces fonctions sont-elles de la responsabilite de Context ?
    objects_arrounds = []
    for point_arround in self.getArroundPointsOfPoint(point):
      if point_arround in self._map:
        for obj in self._map[point_arround]:
          objects_arrounds.append(obj)
    return objects_arrounds
  
  def getArroundPointsOfPoint(self, point):
    pos = point
    pz = pos[0]
    px = pos[1]
    py = pos[2]
    return (
      (pz, px-1, py-1),
      (pz, px,   py-1),
      (pz, px+1, py+1),
      (pz, px-1, py  ),
      (pz, px+1, py  ),
      (pz, px-1, py+1),
      (pz, px,   py+1),
      (pz, px+1, py-1)
    )