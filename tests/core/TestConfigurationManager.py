import unittest
import copy
from synergine.src.core.config.ConfigurationManager import ConfigurationManager


class TestConfigurationManager(unittest.TestCase):

    default_tested_config = {
        'my': {
            'great': {
                'config1': 1,
                'config2': 2
            }
        }
    }

    def test_get_config(self):
        config = ConfigurationManager(copy.deepcopy(self.default_tested_config))
        self.assertEqual(1, config.get('my.great.config1'))
        self.assertEqual(2, config.get('my.great.config2'))

    def test_update_config(self):
        config = ConfigurationManager(copy.deepcopy(self.default_tested_config))
        config.update_config('my.great.config1', 11)
        self.assertEqual(11, config.get('my.great.config1'))
        self.assertEqual(2, config.get('my.great.config2'))

        config.update_config('my', {
            'great': {
                'config1': 9,
                'config2': 0
            }
        })
        self.assertEqual(9, config.get('my.great.config1'))
        self.assertEqual(0, config.get('my.great.config2'))

    def test_set_config(self):
        config = ConfigurationManager(copy.deepcopy(self.default_tested_config))
        config.set_config('a.new.config', 'foo')
        self.assertEqual('foo', config.get('a.new.config'))

    def test_load_config(self):
        config = ConfigurationManager(copy.deepcopy(self.default_tested_config.copy()))
        config.load({
            'my': {
                'great': {
                    'config2': 22,
                    'config3': 3
                }
            },
            'foo': 'bar'
        })
        self.assertEqual(1, config.get('my.great.config1'))
        self.assertEqual(22, config.get('my.great.config2'))
        self.assertEqual(3, config.get('my.great.config3'))
        self.assertEqual('bar', config.get('foo'))
