from synergine.core.SynergyObjectManager import SynergyObjectManager
from synergine.core.exception.NotFoundError import NotFoundError


class Connector():
    """
    Connector is the connection between terminals (Terminal) and Core.
    """

    def __init__(self, synergy_object_manager: SynergyObjectManager, context):
        """
        :param synergy_object_manager: The synergy manager
        :return: void
        """
        self._synergy_object_manager = synergy_object_manager
        self._context = context
        self._terminals = []

    def initialize_terminals(self, terminals_classes, configuration):
        """

        :param terminal_classes: list of Terminal classes
        :param configuration: ConfigurationManager
        :return: void
        """
        for terminal_class in terminals_classes:
            terminal = terminal_class(configuration, self._context, self._synergy_object_manager)
            terminal.initialize()
            self._terminals.append(terminal)

    def cycle(self, actions_done):
        if True: # Stuff est-ce que 25 fps etc
            self._send(actions_done)

    def _send(self, actions_done):
        for terminal in self._terminals:
            terminal.start_of_cycle()
            terminal.receive(actions_done)
            terminal.end_of_cycle()

    def terminate(self):
        for terminal in self._terminals:
            terminal.terminate()

    def get_connection_who_have_to_run_core(self):
        display_who_run_core = None
        for connected_display in self._terminals:
            if connected_display.need_to_run_core():
                if display_who_run_core:
                    raise Exception('Two terminal try to run core. Just one can do it.')
                return connected_display
        return display_who_run_core

    def send_screen_to_connection(self, screen):
        """
        Actually used for Curses
        :param screen:
        :return:void
        """
        display_who_run_core = self.get_connection_who_have_to_run_core()
        if not display_who_run_core:
            raise Exception('Need Terminal object to do that')
        display_who_run_core.initialize_screen(screen)

    def get_terminal(self, terminal_name):
        for terminal in self._terminals:
            if terminal.get_name() == terminal_name:
                return terminal
        raise NotFoundError()