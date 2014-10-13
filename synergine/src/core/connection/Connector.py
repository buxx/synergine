from synergine.src.core.SynergyObjectManager import SynergyObjectManager

class Connector():
    """
    Connector is the connection between terminals (Terminal) and Core.
    """

    def __init__(self, terminals: "list of Terminal", synergy_object_manager: SynergyObjectManager):
        """
        :param terminals: Must be Terminal objects
        :param synergy_object_manager: The synergy manager
        :return: void
        """
        self._synergy_object_manager = synergy_object_manager
        self._terminals = terminals

    def cycle(self):
        if True: # Stuff est-ce que 25 fps etc
            self._send()

    def _send(self):
        for terminal in self._terminals:
            terminal.receive(self._synergy_object_manager)

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
