class Listener(object):

  _listen = None

  def get_listened_class(self):
    return self._listen

  def trigged(self, obj, concerneds_objects, context):
    raise NotImplementedError