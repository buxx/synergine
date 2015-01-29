from module.xyworld.display.object.pygame.PygameImage import PygameImage
from module.traveller.synergy.Traveller import Traveller
from module.traveller.synergy.Town import Town


# TODO: Url relative au fichier
visualisation = {
    'windows': {},
    'objects': {
        Town: {
            'default': PygameImage('/home/bux/Projets/synergine/module/traveller/display/town.png')
        },
        Traveller: {
            'default': PygameImage('/home/bux/Projets/synergine/module/traveller/display/traveller.png')
        }
    }
}