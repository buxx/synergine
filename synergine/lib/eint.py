class IncrementedNamedInt:
    _last_int = 0
    _names = {}

    @classmethod
    def get(cls, name):
        cls._last_int += 1
        cls._names[cls._last_int] = name
        return cls._last_int

    @classmethod
    def name_of(cls, int):
        return cls._names[int]

    @classmethod
    def get_for_name(cls, name):
        for int in cls._names:
            if cls._names[int] == name:
                return int
        raise Exception("Named int not found")