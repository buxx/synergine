class Listener(object):

  _listen = None

  def get_listened_class(self):
    return self._listen

  def trigged(self, obj, context, parameters):
    raise NotImplementedError