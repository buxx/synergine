import unittest
from xyworld.display.DisplayZone import DisplayZone
from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject
from synergine.core.cycle.Context import Context


class TestZone(unittest.TestCase):

    def test_objects_visibility(self):
        zone = DisplayZone(20, 20)
        obj = XyzSynergyObject(object(), Context())
        obj.set_position((0, 10, 10))
        self.assertTrue(zone.point_is_inside(obj.get_position()))
        obj.set_position((0, 10, 21))
        self.assertFalse(zone.point_is_inside(obj.get_position()))