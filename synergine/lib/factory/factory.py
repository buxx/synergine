class Factory:
    class __Factory:
        def __init__(self):
            self._extend_registry = {}
            self._class_registry = {}

        def extend(self, object_name, extend_class, parent_class):
            if object_name not in self._extend_registry:
                self._extend_registry[object_name] = []
            try:
                index_of_existent_extend = self._extend_registry[object_name].index(parent_class)
                self._extend_registry[object_name][index_of_existent_extend] = extend_class
            except ValueError:
                self._extend_registry[object_name].append(extend_class)
                #  try:
                #  index = self._extend_registry[object_name].index(theclass.__bases__[0])
                #     self._extend_registry[object_name][0] = theclass
                # except ValueError:
                #     self._extend_registry[object_name].append(theclass)

        def get_class(self, object_name):
            if object_name not in self._class_registry:
                # Construction d'une classe etendue a partir des sous classes existantes
                # print self._extend_registry[object_name]
                self._class_registry[object_name] = type('Final' + object_name,
                                                         tuple(self._extend_registry[object_name]), {})
            return self._class_registry[object_name]

    instance = None

    def __init__(self):
        if not Factory.instance:
            Factory.instance = Factory.__Factory()

    def __getattr__(self, name):
        return getattr(self.instance, name)