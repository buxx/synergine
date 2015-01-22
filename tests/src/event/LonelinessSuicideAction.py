from synergine.src.synergy.event.Action import Action
from tests.src.event.LonelinessSuicideEvent import LonelinessSuicideEvent
from tests.src.event.TooMuchBeansAction import TooMuchBeansAction
from synergine.metas import metas
from tests.src.TestSimulation import TestSimulation

class LonelinessSuicideAction(Action):

    _listen = LonelinessSuicideEvent
    _depend = [TooMuchBeansAction]

    def run(self, obj, collection, context):
        collection.remove_object(obj)
        #metas.list.remove(TestSimulation.STATE, obj.get_id(), TestSimulation.COMPUTABLE)
        #metas.list.remove(TestSimulation.STATE, TestSimulation.COMPUTABLE, obj.get_id())