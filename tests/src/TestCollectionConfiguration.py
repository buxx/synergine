from synergine.src.synergy.collection.Configuration import Configuration
from tests.src.TestSynergyObject import TestSynergyObject
from synergine.metas import metas
from tests.src.TestSimulation import TestSimulation


class TestCollectionConfiguration(Configuration):

    def get_start_objects(self):
        objs_setup = (
            ('john', 2, 2),
            ('boby', 2, 5),
            ('cora', 2, 10),
            ('mara', 2, 20),
        )

        objects = []
        for obj_setup in objs_setup:
            obj = TestSynergyObject()
            obj.setUp(obj_setup[0], obj_setup[1], obj_setup[2])
            objects.append(obj)
            metas.list.add(TestSimulation.STATE, obj.get_id(), TestSimulation.COMPUTABLE)
            metas.list.add(TestSimulation.STATE, TestSimulation.COMPUTABLE, obj.get_id())

        return objects