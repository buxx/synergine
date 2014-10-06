class SynergyObjectManager(object):
  #todo refactoriser getcoll

  def __init__(self, simulations):
    self._simulations = simulations
  
  def getSimulations(self):
    return self._simulations

  def getCollections(self):
    collections = []
    for simulation in self._simulations:
      for collection in simulation.getCollections():
        collections.append(collection)
    return collections
  
  def getComputableObjects(self):
    computable_objects = []
    for simulation in self._simulations:
      for collection in simulation.getCollections():
        for collection_computable_object in collection.getComputableObjects():
          computable_objects.append(collection_computable_object)
    return computable_objects
  
  def getObjects(self):
    objects = []
    for simulation in self._simulations:
      for collection in simulation.getCollections():
        for collection_object in collection.getObjects():
          objects.append(collection_object)
    return objects

  def getListeners(self):
    listeners = []
    for simulation in self._simulations:
      for listener in simulation.get_listeners():
        listeners.append(listener)
    return listeners

  # todo: la func ci-dessous sont-elles a leurs place ?
  def getObjectsToDisplay(self):
    objects_to_display = []
    for simulation in self._simulations:
      for collection in simulation.getCollections():
        for collection_object_to_display in collection.getObjectsToDisplay():
          objects_to_display.append(collection_object_to_display)
    return objects_to_display