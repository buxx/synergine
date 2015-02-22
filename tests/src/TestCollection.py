from synergine.synergy.collection.SynergyCollection import SynergyCollection
from tests.src.event.TooMuchBeansAction import TooMuchBeansAction
from tests.src.event.MakeBeansProfitAction import MakeBeansProfitAction
from tests.src.event.LonelinessSuicideAction import LonelinessSuicideAction
from tests.src.cst import COL_COMPUTABLE
from tests.src.event.LonelinessSuicideAction import LonelinessSuicideAction
from synergine.core.Signals import Signals

class TestCollection(SynergyCollection):

    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [MakeBeansProfitAction, TooMuchBeansAction, LonelinessSuicideAction]

        # hack; to prevent cycle import bug:
        Signals.signal(LonelinessSuicideAction).connect(lambda obj, context: \
            context.metas.collections.remove(obj.get_id(), COL_COMPUTABLE))
