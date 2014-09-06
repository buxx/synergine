class SynergyObjectManager(object):
  
  def __init__(self):
    self._collections = []
  
  def initCollection(self, name, collection):
    # TODO: name ?
    self._collections.append(collection)
  
  def getComputableObjects(self):
    computable_objects = []
    for collection in self._collections:
      for collection_computable_object in collection.getComputableObjects():
        computable_objects.append(collection_computable_object)
    return computable_objects