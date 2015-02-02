class Map:

    def __init__(self):
        self._map = {
            'objects': {}
        }

    def get_object(self, object_id):
        return self._map['objects'][object_id]

    def add_object(self, obj):
        self._map['objects'][obj.get_id()] = obj

    def remove_object(self, obj):
        del(self._map['objects'][obj.get_id()])