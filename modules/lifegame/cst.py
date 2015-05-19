from synergine.lib.eint import IncrementedNamedInt

ALIVE = IncrementedNamedInt.get('lifegame.alive')
DIED = IncrementedNamedInt.get('lifegame.died')

COL_DIED = IncrementedNamedInt.get('lifegame.col.died')
COL_ALIVE = IncrementedNamedInt.get('lifegame.col.alive')
