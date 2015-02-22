from synergine.synergy.collection.Configuration import Configuration
from tests.src.TestSynergyObject import TestSynergyObject
from tests.src.cst import COL_COMPUTABLE, COMPUTABLE


class TestCollectionConfiguration(Configuration):

    def get_start_objects(self, collection, context):
        objs_setup = (
            ('john', 2, 2),
            ('boby', 2, 5),
            ('cora', 2, 10),
            ('mara', 2, 20),
        )

        objects = []
        for obj_setup in objs_setup:
            obj = TestSynergyObject(context)
            obj.setUp(obj_setup[0], obj_setup[1], obj_setup[2])
            objects.append(obj)
            context.metas.collections.add(obj.get_id(), COL_COMPUTABLE)
            context.metas.states.add(obj.get_id(), COMPUTABLE)
            context.metas.states.add(COMPUTABLE, obj.get_id())

        return objects