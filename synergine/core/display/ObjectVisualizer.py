from synergine.core.config.ConfigurationManager import ConfigurationManager
from synergine.synergy.object.SynergyObject import SynergyObject
from synergine.core.exception.NotFoundError import NotFoundError


class ObjectVisualizer():
    """
    TODO: Il y a eu un ajout, notion de surface directement en plus des objets.
          Du coups c'est sale et pas DRY. A reviser.
    """

    def __init__(self, config: dict, context):
        config_manager = ConfigurationManager(config)
        self._visualisation_configuration = config_manager.get('objects', {})
        self._surface_configuration = config_manager.get('surfaces', {})
        self._objects_class_mapped = {}
        self._context = context
        self._callback_position = config_manager.get('callbacks.position', 0)

    def get_visual(self, obj: SynergyObject):
        visualisation_definition = self._get_visual_definition(obj)
        if 'callbacks' in visualisation_definition:
            for callback in visualisation_definition['callbacks']:
                callback_return = callback(obj, self._context)
                # TODO: Exception au lieu de False
                if callback_return is not False:
                    return self._apply_modifiers_on_visual(visualisation_definition, obj, callback_return)
        return self._apply_modifiers_on_visual(visualisation_definition, obj, visualisation_definition['default'])

    def _apply_modifiers_on_visual(self, visualisation_definition, obj, visual):
        new_visual = visual
        if 'modifiers' in visualisation_definition:
            for modifier in visualisation_definition['modifiers']:
                new_visual = modifier(obj, self._context, visual)
        return new_visual

    def get_surface(self, surface_name, parameters={}):
        surface_definition = self._get_surface_definition(surface_name)
        if 'callbacks' in surface_definition:
            for callback in surface_definition['callbacks']:
                callback_return = callback(parameters, self._context)
                # TODO: Exception au lieu de False
                if callback_return is not False:
                    return callback_return.get_surface()
        return surface_definition['default'].get_surface()

    def get_for_position(self, position, objects):
        if self._callback_position:
            return self._callback_position(position, objects, self._context)
        return None, []

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

    def _get_surface_definition(self, surface_name):
        return self._surface_configuration[surface_name]