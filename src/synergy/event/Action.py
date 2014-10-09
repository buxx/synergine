class Action(object):

  _listen = None

  @classmethod
  def get_listened_class(cls):
    return cls._listen

  def __init__(self, parameters):
    self._parameters = parameters
    self._obj = None

  def set_object(self, obj):
    self._obj = obj

  def run(self, collection, context):
    raise NotImplementedError