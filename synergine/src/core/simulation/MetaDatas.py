from synergine.src.core.simulation.MetaCollections import MetaCollections


class MetaDatas:

  def __init__(self):
    self._state_lists = MetaCollections()
    self._object_states = MetaCollections()

  def set(self, obj, state):
    self._state_lists.add(state, obj)
    self._object_states.add(obj, state)

  def unset(self, obj, state):
    try:
      self._state_lists.remove(state, obj)
      self._object_states.remove(obj, state)
    except ValueError:
      raise Exception("Unable to find \"%s\" in meta data \"%s\". It must be added in these meta data before." % (obj, state))

  def state_have(self, state, obj):
    return self._state_lists.is_in(state, obj)

  def have_state(self, obj, state):
    return self._object_states.is_in(obj, state)
