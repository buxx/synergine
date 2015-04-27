from synergine.core.exception.NotFoundError import NotFoundError


class ConfigurationManager():
    """
    Management of dict based configuration data
    """

    def __init__(self, config: dict={}):
        self._configs = config

    def get(self, config_name: "the.config.name", default=None):
        inceptions = config_name.split('.')
        config = self._configs
        for inception in inceptions:
            if inception in config:
                config = config[inception]
            elif default is not None:
                return default
            else:
                raise NotFoundError('Config "'+config_name+'"" not found')
        return config

    def update_config(self, config_name: "the.config.name", config_value):
        inceptions = config_name.split('.')
        inception_count = 0
        parent_config = self._configs
        config = self._configs
        for inception in inceptions:
            inception_count += 1
            if inception in config:
                parent_config = config
                config = config[inception]
            else:
                raise Exception('Config "'+config_name+'"" not found')
        parent_config[inception] = config_value

    def set_config(self, config_name: "the.config.name", config_value):
        inceptions = config_name.split('.')
        config = self._configs
        for inception in inceptions:
            if inception in config:
                config = config[inception]
            elif inceptions.index(inception)+1 == len(inceptions):
                config[inception] = config_value
            else:
                config[inception] = {inceptions.__getitem__(inceptions.index(inception)+1): {}}
                config = config[inception]

    def load(self, config_to_load):
        self._configs = self._merge(self._configs, config_to_load)

    def _merge(self, a, b, path=None):
        "merges b into a"
        if path is None:
            path = []
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    self._merge(a[key], b[key], path + [str(key)])
                elif a[key] == b[key]:
                    pass
                else:
                    a[key] = b[key]
            else:
                a[key] = b[key]
        return a