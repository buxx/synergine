class Mechanism():

    def __init__(self, events):
        self._events = events
        self._events_parameters = {}

    def run(self, objects, context):
        self._prepare_objects_parameters(objects, context)
        self._run_events(objects, context)

    def _prepare_objects_parameters(self, objects, context):
        # Quelque soit le nombre d'event le mechanisme ne calcule qu'une fois les donnees destines aux events
        self._events_parameters = {}
        for obj in objects:
            self._events_parameters[obj] = self._get_object_event_parameters(obj, context)

    def _run_events(self, objects, context):
        for event in self._events:
            for obj in objects:
                event.observe(obj, context, self._events_parameters[obj])

    def _get_object_event_parameters(self, obj, context):
        return {}
