class Terminal():
    """
    Obj who receive synergine data at each cycle
    """

    def __init__(self):
        self._encapsuled_run = False

    def encapsulate_run(self, run_function):
        self._encapsuled_run = True

    def have_encapsulated_run(self):
        return self._encapsuled_run

    def need_to_run_core(self):
        return False

    # TODO: Renommer
    def initialize_screen(self, screen):
        pass

    def receive(self, synergy_object_manager):
        pass

    def terminate(self):
        pass