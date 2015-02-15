class Action():

    _listen = None
    _depend = []

    @classmethod
    def get_listened_class(cls):
        return cls._listen

    @classmethod
    def get_dependencies(cls):
        return cls._depend

    def __init__(self, object_id, parameters):
        self._object_id  = object_id
        self._parameters = parameters

    def get_object_id(self):
        return self._object_id

    def prepare(self, context):
      """
      Prepare data for action run. This part is executed in sub processes.
      :return: void
      """
      pass

    def run(self, obj, collection, context, synergy_manager):
        raise NotImplementedError