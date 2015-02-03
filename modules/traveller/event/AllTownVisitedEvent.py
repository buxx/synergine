from synergine.synergy.event.Event import Event
from synergine.core.simulation.mechanism.Mechanism import Mechanism
from traveller.synergy.Traveller import Traveller
from traveller.synergy.Town import Town

class AllTownVisitedEvent(Event):
    """
    Le traveller a visité toutes les towns
    """

    def __init__(self, actions):
        super().__init__(actions)
        self._concerneds = [Traveller]
        self._mechanism = Mechanism

    def _object_match(self, obj, context, parameters={}):
        if super()._object_match(obj, context, parameters):
            if self._traveller_visited_all_town(obj, context.get_objects_by_type(Town)):
              return True
        return False

    def _traveller_visited_all_town(self, traveller, towns):
        for town in towns:
            try:
                traveller.get_towns().index(town)
            except ValueError:
                return False
        return True