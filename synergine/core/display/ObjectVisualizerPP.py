from synergine.core.config.ConfigurationManager import ConfigurationManager
from synergine.synergy.object.SynergyObject import SynergyObject
from synergine.core.exception.NotFoundError import NotFoundError


class ObjectVisualizer():

    def __init__(self, config: dict):
        config_manager = ConfigurationManager(config)
        self._visualisation_configuration = config_manager.get('objects', {})
        self._objects_class_mapped = {}
<<<<<<< Updated upstream
=======
        self._context = context
>>>>>>> Stashed changes

    def get_visual(self, obj: SynergyObject):
        visualisation_definition = self._get_visual_definition(obj)
        if 'callbacks' in visualisation_definition:
            for callback in visualisation_definition['callbacks']:
                callback_return = callback(obj)
                if callback_return is not False:
                    return callback_return
        return visualisation_definition['default']

# TODO: fix bug: on doit mettre en cache dans self._objects_class_mapped le dict {default... et non pas le resultat
    def _get_visual_definition_for_class(self, class_name, obj):
        if obj.__class__ in self._visualisation_configuration:
            return self._visualisation_configuration[obj.__class__]
        for object_visualisation_class in self._visualisation_configuration:
            if isinstance(obj, object_visualisation_class):
                return self._visualisation_configuration[object_visualisation_class]
        raise NotFoundError()

    def _get_default_visualisation(self):
        if SynergyObject not in self._visualisation_configuration:
            raise Exception("Enable to found SynergyObject visualisation")
        return self._visualisation_configuration[SynergyObject]['default']

    def _get_visual_definition(self, obj: SynergyObject):
        class_name = obj.__class__.__name__
        if class_name not in self._objects_class_mapped:
            try:
                object_visualisation_definition = self._get_visual_definition_for_class(class_name, obj)
            except NotFoundError:
                object_visualisation_definition = self._get_default_visualisation()
            self._objects_class_mapped[class_name] = object_visualisation_definition

        return self._objects_class_mapped[class_name]