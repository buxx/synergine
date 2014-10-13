class ConfigurationManager():
    """
    Management of dict based configuration data
    """

    def __init__(self, config: dict):
        self._configs = config

    def get(self, config_name: "the.config.name", default=None):
        inceptions = config_name.split('.')
        config = self._configs
        for inception in inceptions:
            if inception in config:
                config = config[inception]
            elif default:
                return default
            else:
                raise Exception('Config "'+config_name+'"" not found')
        return config
