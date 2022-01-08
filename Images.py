import os

import pygame


class Button():
    Stop_IMAGE = pygame.image.load(os.path.join('img', 'stop.png'))
    Stop = pygame.transform.scale(Stop_IMAGE, (70, 70))

    def __init__(self):
        width = self.Stop.get_width()
        height = self.Stop.get_height()
        self.image = pygame.transform.scale(self.Stop, (int(width * 0.8), int(height * 0.8)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.clicked = False

    def draw(self, screen):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # draw Button:
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


class PokemonImages:
    # Pikachu:
    Pikachu_IMAGE = pygame.image.load(os.path.join('img', 'Pikachu.png'))
    Pikachu = pygame.transform.scale(Pikachu_IMAGE, (50, 50))
    # Charizard:
    Charizard_IMAGE = pygame.image.load(os.path.join('img', 'Charizard.png'))
    Charizard = pygame.transform.scale(Charizard_IMAGE, (50, 50))
    # Jigglypuff:
    Jigglypuff_IMAGE = pygame.image.load(os.path.join('img', 'Jigglypuff.png'))
    Jigglypuff = pygame.transform.scale(Jigglypuff_IMAGE, (50, 50))
    # Bulbasaur:
    Bulbasaur_IMAGE = pygame.image.load(os.path.join('img', 'Bulbasaur.png'))
    Bulbasaur = pygame.transform.scale(Bulbasaur_IMAGE, (50, 50))
    # Squirtle:
    Squirtle_IMAGE = pygame.image.load(os.path.join('img', 'Squirtle.png'))
    Squirtle = pygame.transform.scale(Squirtle_IMAGE, (50, 50))
    # Venusaur:
    Venusaur_IMAGE = pygame.image.load(os.path.join('img', 'Venusaur.png'))
    Venusaur = pygame.transform.scale(Venusaur_IMAGE, (50, 50))
    # Typhlosion:
    Typhlosion_IMAGE = pygame.image.load(os.path.join('img', 'Typhlosion.png'))
    Typhlosion = pygame.transform.scale(Typhlosion_IMAGE, (50, 50))
    # Zapdos:
    Zapdos_IMAGE = pygame.image.load(os.path.join('img', 'Zapdos.png'))
    Zapdos = pygame.transform.scale(Zapdos_IMAGE, (50, 50))
    # Totodile:
    Totodile_IMAGE = pygame.image.load(os.path.join('img', 'Totodile.png'))
    Totodile = pygame.transform.scale(Totodile_IMAGE, (50, 50))
    # Pyroar:
    Pyroar_IMAGE = pygame.image.load(os.path.join('img', 'Pyroar.png'))
    Pyroar = pygame.transform.scale(Pyroar_IMAGE, (50, 50))
    # Eevee:
    Eevee_IMAGE = pygame.image.load(os.path.join('img', 'Eevee.png'))
    Eevee = pygame.transform.scale(Eevee_IMAGE, (50, 50))

    def draw(self, screen, pokemons, my_scale):
        for p in pokemons:
            if p.value == 5:
                screen.blit(self.Squirtle,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
            elif p.value == 6:
                screen.blit(self.Bulbasaur,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
            elif p.value == 7:
                screen.blit(self.Jigglypuff,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
            elif p.value == 8:
                screen.blit(self.Eevee,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
            elif p.value == 9:
                screen.blit(self.Zapdos,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
            elif p.value == 10:
                screen.blit(self.Totodile,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
            elif p.value == 11:
                screen.blit(self.Typhlosion,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
            elif p.value == 12:
                screen.blit(self.Venusaur,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
            elif p.value == 13:
                screen.blit(self.Charizard,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
            elif p.value == 14:
                screen.blit(self.Pyroar,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
            elif p.value >= 15:
                screen.blit(self.Pikachu,
                            (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))

class AgentsImages:
    Jessie_IMAGE = pygame.image.load(
        os.path.join('img', 'Jessie.png'))
    Jessie = pygame.transform.scale(
        Jessie_IMAGE, (50, 60))
    James_IMAGE = pygame.image.load(
        os.path.join('img', 'James.png'))
    James = pygame.transform.scale(
        James_IMAGE, (50, 60))
    Meowth_IMAGE = pygame.image.load(
        os.path.join('img', 'Meowth.png'))
    Meowth = pygame.transform.scale(
        Meowth_IMAGE, (50, 60))

    def draw(self, screen, agents):
        for agent in agents:
            if agent.id == 0:
                screen.blit(self.James, (int(agent.pos.x), int(agent.pos.y)))
            if agent.id == 1:
                screen.blit(self.Jessie, (int(agent.pos.x), int(agent.pos.y)))
            if agent.id == 2:
                screen.blit(self.Meowth, (int(agent.pos.x), int(agent.pos.y)))

