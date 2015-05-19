from synergine.core.exceptions import NotConcernedEvent
from synergine.core.simulation.mechanism.Mechanism import Mechanism
from synergine.cst import COL_ALL


class Event():
    """
    Event are called by mechanisms and trig associated actions if conditions matches.
    """

    _mechanism = Mechanism
    """Mechanism class who run this event with prepared parameters"""
    _concern = COL_ALL
    """The COL id of concerned synergies objects"""
    _each_cycle = 1
    """Event ca be executed each x cycle if needed"""

    def __init__(self, actions):
        self._actions = actions

    @classmethod
    def get_mechanism(cls):
        """

        :return: Mechanism class who will run this event
        :rtype: Mechanism
        """
        return cls._mechanism

    @classmethod
    def get_concern(cls):
        """

        :return: COL name if concerned synergies objects
        """
        return cls._concern

    @classmethod
    def get_each_cycle(cls):
        """

        :return: The number of each cycle where execute this event
        """
        return cls._each_cycle

    def observe(self, object_id, context, parameters={}):
        """

        Return actions who have to be executed.

        :param object_id: The id of observed synergy object
        :param context: The Context
        :param parameters: Mechanism prepared dict of parameters
        :return: list of actions
        :rtype: list (of Action)
        """
        active_actions = []
        try:
            parameters = self._prepare(object_id, context, parameters)
            for action in self._actions:
                action_object = action(object_id, parameters)
                active_actions.append(action_object)
        except NotConcernedEvent:
            pass  # Object not concerned by this event

        return active_actions

    def _prepare(self, object_id, context, parameters={}):
        """

        Return dict with parameters for actions

        :param object_id: The id of observed synergy object
        :param context: The Context
        :param parameters: Mechanism prepared dict of parameters
        :raise: NotConcernedEvent
        :return:
        """
        raise NotImplementedError()