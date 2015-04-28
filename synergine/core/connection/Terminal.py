from synergine.core.exception.NotFoundError import NotFoundError


class Terminal():
    """
    Obj who receive synergine data at each cycle
    """

    _name = None

    @classmethod
    def get_name(cls):
        if not cls._name:
            raise Exception("Terminal must be named")
        return cls._name

    def __init__(self, config, context, synergy_manager):
        """

        :param config: ConfigurationManager
        :return: void
        """
        self._encapsuled_run = False
        self._config = config
        self._context = context
        self._synergy_manager = synergy_manager

    def _get_config(self, config_name, default=None):
        try:
            return self._config.get('terminal.'+self.get_name()+'.'+config_name)
        except NotFoundError:
            pass
        try:
            return self._config.get('terminal.__default__.'+config_name)
        except NotFoundError:
            pass
        try:
            return self._config.get(config_name)
        except NotFoundError:
            pass
        if default is not None:
            return default
        raise NotFoundError("Can't found config ", config_name)

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

    def initialize_screen(self, screen):
        pass

    def receive(self, actions_done):
        pass

    def terminate(self):
        pass