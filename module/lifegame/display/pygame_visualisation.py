from synergine.src.synergy.object.SynergyObject import SynergyObject
from synergine.src.display.object.pygame.PygameImage import PygameImage
from module.lifegame.synergy.object.Cell import Cell

# TODO: Url relative au fichier
image_cell_full = PygameImage('/home/bux/Projets/synergine/module/lifegame/display/pygame/cha3.png')
image_cell_medium = PygameImage('/home/bux/Projets/synergine/module/lifegame/display/pygame/cha2.png')
image_cell_small = PygameImage('/home/bux/Projets/synergine/module/lifegame/display/pygame/cha.png')
image_cell_dead = PygameImage('/home/bux/Projets/synergine/module/lifegame/display/pygame/cha0.png')

def is_old_cell(cell):
    if cell.get_is_alive_since() == 1:
        return image_cell_small
    if cell.get_is_alive_since() == 2:
        return image_cell_medium
    if cell.get_is_alive_since() > 2:
        return image_cell_full

    if cell.get_is_died_since() == 1:
        return image_cell_dead

    if not cell.is_alive():
        return image_cell_dead

    return False

visualisation = {
    'window': {},
    'objects': {
        Cell: {
            'default': image_cell_small,
            'callbacks': [is_old_cell]
        }
    }
}