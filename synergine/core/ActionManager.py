from synergine.core.exception.NotFoundError import NotFoundError


class ActionManager():
    """
    Manaer of Action object
    """

    def get_steps_for_actions(self, actions: list):
        """
        Return a list of hierarchical list of action where an action is always
        placed in list after list containing his Action dependencies
        :param actions: list of Action
        :return: list of steps where step contain list of Event
        """
        actions_copy = actions[:]
        steps = [[]]
        count = 0
        for action in actions_copy:
            count += 1
            if count > 10000:  # TODO: hard code
                raise Exception("Impossible to find dependencies of action", actions)
            last_action = action
            action_dependencies = action.get_dependencies()
            if action_dependencies:
                try:
                    step_index = self._get_step_index_for_dependencies(steps, action_dependencies)
                    if step_index is not None:
                        try:
                            steps[step_index+1].append(action)
                        except IndexError:
                            steps.append([action])
                    else:
                        step = []
                        step.extend(action_dependencies)
                        steps.append(step)
                # Si une des dependences n'est pas encore dans les steps, on s'occupera de cette action plus tard
                except NotFoundError:
                    # TODO: Prevoir le cas ou la dependance n'existera jamais dans la liste et lever une erreur
                    actions_copy.append(action)
            else:
                steps[0].append(action)
        return steps

    def _get_step_index_for_dependencies(self, steps, dependencies):
        step_index_found = None
        for dependency in dependencies:
            step_index = self._get_step_index_for_dependency(steps, dependency)
            if step_index_found is None:
                step_index_found = step_index
            else:
                if step_index > step_index_found:
                    step_index_found = step_index
        return step_index_found

    def _get_step_index_for_dependency(self, steps, dependency):
        for step_index, step_actions in enumerate(steps):
            for step_action in step_actions:
                if issubclass(step_action, dependency):
                    return step_index
        raise NotFoundError()