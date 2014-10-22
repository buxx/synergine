class Terminal():
    """
    Obj who receive synergine data at each cycle
    """

    def __init__(self, config={}):
        self._encapsuled_run = False
        self._config = config

    def encapsulate_run(self, run_function):
        self._encapsuled_run = True

    def initialize(self):
        pass

    def have_encapsulated_run(self):
        return self._encapsuled_run

    def need_to_run_core(self):
        return False

    def start_of_cycle(self):
        pass

    def end_of_cycle(self):
        pass

    # TODO: Renommer
    def initialize_screen(self, screen):
        pass

    def receive(self, synergy_object_manager):
        pass

    def terminate(self):
        pass