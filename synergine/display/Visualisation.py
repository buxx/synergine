class Visualisation():

    @staticmethod
    def get_default_visualisation():
        return {
            'window': {},
            'callbacks': {},
            'surfaces': {},
            'objects': {}
        }

    def __init__(self, visualisation_config):
        self._visualisation_config = visualisation_config

    def update_objects_images(self, objects_images):
        for object_class in objects_images:
            object_image = objects_images[object_class]
            self._update_object_config(object_class, object_image)

    def _update_object_config(self, object_class, object_image):
        if object_class not in self._visualisation_config['objects']:
            self._visualisation_config['objects'][object_class] = {
                'default': None,
                'callbacks': [],
                'modifiers': []
            }
        self._visualisation_config['objects'][object_class]['default'] = object_image
