import unittest
from src.core.ActionManager import ActionManager
from tests.src.event.test_actions import A,B,C,D,E,F,G,H
from random import shuffle


class TestActionManager(unittest.TestCase):

    def test_action_manager(self):
        action_manager = ActionManager()
        actions = [A, B, C, D, E, F, G, H]
        steps_correct_order = [
            ['A', 'D', 'G'],
            ['B'],
            ['C', 'H'],
            ['F'],
            ['E']
        ]
        self.assertEqual(steps_correct_order, self._get_class_name_representation(action_manager.get_steps_for_actions(actions)))

        for i in range(10):
            shuffle(actions)
            self.assertEqual(steps_correct_order, self._get_class_name_representation(action_manager.get_steps_for_actions(actions)))

    def _get_class_name_representation(self, steps):
        steps_representation = []
        for step in steps:
            step_representation = []
            for action in step:
                step_representation.append(action.__name__)
            steps_representation.append(sorted(step_representation))
        return steps_representation