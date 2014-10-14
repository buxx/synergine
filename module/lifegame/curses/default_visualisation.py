from synergine.src.synergy.object.SynergyObject import SynergyObject
from synergine.src.display.object.TextTraceVisualisation import TextTraceVisualisation
from module.lifegame.synergy.object.Cell import Cell


def is_old_cell(cell):
    if cell.get_is_alive_since() == 1:
        return TextTraceVisualisation('o')
    if cell.get_is_alive_since() == 2:
        return TextTraceVisualisation('O')
    if cell.get_is_alive_since() > 2:
        return TextTraceVisualisation('0')
    #return TextTraceVisualisation(str(cell.get_is_alive_since()))
    return False


visualisation = {
    'window': {},
    'objects': {
        #SynergyObject: {
        #    'default': TextTraceVisualisation('*')
        #},
        Cell: {
            'default': TextTraceVisualisation('*'),
            'callbacks': [is_old_cell]
        }
    }
}