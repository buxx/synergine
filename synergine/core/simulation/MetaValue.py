class MetaValue:

  def __init__(self):
    self._metas = {}

  def reset(self):
    self._metas = {}

  def _get_metas(self, name):
    if name not in self._metas:
      self._metas[name] = {}
    return self._metas[name]

  def set(self, name, subject, value):
    metas = self._get_metas(name)
    metas[subject] = value
  
  def unset(self, name, subject):
    metas = self._get_metas(name)
    del(state[subject])
  
  def have(self, name, subject):
    metas = self._get_metas(name)
    return subject in metas
    
  def get(self, name, subject):
    metas = self._get_metas(name)
    return metas[subject]