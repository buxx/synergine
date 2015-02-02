class MetaCollections:

  def __init__(self):
    self._metas = {}

  def reset(self):
    self._metas = {}

  def _get_collection(self, name):
    if name not in self._metas:
      self._metas[name] = {}
    return self._metas[name]

  def get(self, name, subject, allow_empty=False):
    metas = self._get_collection(name)
    if subject not in metas and allow_empty:
      metas[subject] = []
    return metas[subject]

  def add(self, name, subject, value):
    collection = self.get(name, subject, allow_empty=True)
    collection.append(value)

  def remove(self, name, subject, value):
    collection = self.get(name, subject)
    collection.remove(value)

  def have(self, name, subject, value):
    collection = self.get(name, subject)
    return value in collection
