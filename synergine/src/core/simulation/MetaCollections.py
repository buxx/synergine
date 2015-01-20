class MetaCollections:

  def __init__(self):
    self._collections = {}

  def get_collection(self, collection_name):
    if collection_name not in self._collections:
      self._collections[collection_name] = []
    return self._collections[collection_name]

  def add(self, collection_name, meta):
    collection = self.get_collection(collection_name)
    collection.append(meta)

  def remove(self, collection_name, meta):
    object_meta = self.get_collection(collection_name)
    object_meta.remove(meta)

  def is_in(self, collection_name, meta):
    collection = self.get_collection(collection_name)
    return meta in collection
