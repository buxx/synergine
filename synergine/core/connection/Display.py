from synergine.core.connection.Terminal import Terminal
from synergine.core.display.ObjectVisualizer import ObjectVisualizer


class Display(Terminal):
    """
    Graphical visualisation Terminal
    """

    def __init__(self, config, context, synergy_manager):
        super().__init__(config, context, synergy_manager)
        self._object_visualizer = ObjectVisualizer(self._get_config('visualisation', {}), self._context)
