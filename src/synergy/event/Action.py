class Action():

    _listen = None
    _depend = []

    @classmethod
    def get_listened_class(cls):
        return cls._listen

    @classmethod
    def get_dependencies(cls):
        return cls._depend

    def __init__(self, parameters):
        self._parameters = parameters
        self._obj = None

    def set_object(self, obj):
        self._obj = obj

    def run(self, collection, context):
        raise NotImplementedError