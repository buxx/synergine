import unittest
from synergine.src.core.display.DisplayZone import DisplayZone
from synergine.src.synergy.object.SynergyObject import SynergyObject

class TestZone(unittest.TestCase):

    def test_objects_visibility(self):
        zone = DisplayZone(20, 20)
        obj = SynergyObject()
        obj.add_trace((0, 10, 10))
        self.assertTrue(zone.point_is_inside(obj.get_point()))
        obj.add_trace((0, 10, 21))
        self.assertFalse(zone.point_is_inside(obj.get_point()))