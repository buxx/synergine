from synergine.core.connection.Terminal import Terminal
from synergine.core.display.ObjectVisualizer import ObjectVisualizer


class Display(Terminal):
    """
    Graphical visualisation Terminal
    """

<<<<<<< Updated upstream
    def __init__(self, config):
        super().__init__(config)
        self._object_visualizer = ObjectVisualizer(self._get_config('visualisation', {}))
=======
    def __init__(self, config, context):
        super().__init__(config, context)
        self._object_visualizer = ObjectVisualizer(self._get_config('visualisation', {}), self._context)
>>>>>>> Stashed changes
