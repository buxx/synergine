class SynergyObjectManager(object):
  
  def __init__(self):
    self._collections = []
  
  def initCollection(self, name, collection):
    # TODO: name ?
    self._collections.append(collection)
  
  def getComputableObjects(self):
    computable_objects = []
    for collection in self._collections:
      computable_objects.append(collection.getComputableObjects())
    return computable_objects