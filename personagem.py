import pygame
from pygame.locals import *

class Personagem(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('homem_terno/sprite_0.png'))
        self.sprites.append(pygame.image.load('homem_terno/sprite_1.png'))
        self.sprites.append(pygame.image.load('homem_terno/sprite_2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32*7, 32*7))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 200

    def update(self):
        self.atual += 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32*7, 32*7))