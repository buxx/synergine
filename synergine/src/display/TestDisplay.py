from synergine.src.core.connection.Display import Display


class TestDisplay(Display):

    _name = "test"

    def draw_object(self, obj, point):
        pass

    def terminate(self):
        pass