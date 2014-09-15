class SynergyObjectManager(object):
  
  def __init__(self, collections):
    self._collections = collections
  
  def getCollections(self):
    return self._collections
  
  def getComputableObjects(self):
    computable_objects = []
    for collection in self._collections:
      for collection_computable_object in collection.getComputableObjects():
        computable_objects.append(collection_computable_object)
    return computable_objects
  
  def getObjects(self):
    objects = []
    for collection in self._collections:
      for collection_object in collection.getObjects():
        objects.append(collection_object)
    return objects
  
  def getObjectsToDisplay(self):
    objects_to_display = []
    for collection in self._collections:
      for collection_object_to_display in collection.getObjectsToDisplay():
        objects_to_display.append(collection_object_to_display)
    return objects_to_display