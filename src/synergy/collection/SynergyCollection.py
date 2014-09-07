class SynergyCollection(object):
  
  def __init__(self):
    self._objects = ['Foo', 'Bar', 'Baz', 'Biz']
  
  def getComputableObjects(self):
    return self._objects