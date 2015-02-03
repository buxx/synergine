import unittest
from xyworld.display.DisplayZone import DisplayZone
from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject

class TestZone(unittest.TestCase):

    def test_objects_visibility(self):
        zone = DisplayZone(20, 20)
        obj = XyzSynergyObject()
        obj.add_trace((0, 10, 10))
        self.assertTrue(zone.point_is_inside(obj.get_point()))
        obj.add_trace((0, 10, 21))
        self.assertFalse(zone.point_is_inside(obj.get_point()))