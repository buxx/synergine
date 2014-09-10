class Context(object):
  
  def __init__(self, synergy_object_manager):
    self._synergy_object_manager = synergy_object_manager
    self._map = {}
  
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