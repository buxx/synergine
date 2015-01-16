class Action():

    _listen = None
    _depend = []

    @classmethod
    def get_listened_class(cls):
        return cls._listen

    @classmethod
    def get_dependencies(cls):
        return cls._depend

    def __init__(self, obj, parameters):
        self._object_id  = obj.get_id()
        self._parameters = parameters

    def get_object_id(self):
        return self._object_id

    def run(self, obj, collection, context):
        raise NotImplementedError