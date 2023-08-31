import pygame
import os
from pygame.locals import *
from random import randrange

LARGURA = 640
ALTURA = 480

class Cacto(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet, escolha):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (LARGURA, ALTURA - 64)
        self.rect.x = LARGURA
        self.escolha = escolha
        self.velocidade = 10

    def update(self):

        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = LARGURA
            self.rect.x -= self.velocidade

class Chao(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet, x_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 64
        self.rect.x = x_pos

    def update(self):

        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= 10

class Nuvens(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((32*7, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = LARGURA - randrange(30, 300, 90)
        self.velocidade = 10

    def update(self):

        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= self.velocidade #speed of the cloud

class Dino(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, diretorio_sons):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'jump_sound.wav'))
        self.som_pulo.set_volume(1)

        for i in range (3):
            img = sprite_sheet.subsurface((i*32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)
        
        self.pulo = False
        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (100, ALTURA - 64) #posicionando a sprite na tela
        self.posY_inicial = ALTURA - 64 - 96 // 2
    
    def update(self):

        if self.pulo == True:
            if self.rect.y <= self.posY_inicial - 150:
                self.pulo = False
            self.rect.y -= 15
        else:
            if self.rect.y < self.posY_inicial:
                self.rect.y += 15
            else:
                self.rect.y = self.posY_inicial
        
        if self.index_lista >= 2:
            self.index_lista = 0 
        self.index_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.index_lista)] #atualizando a imagem do dinossauro

    def pula(self):
        self.pulo = True
        self.som_pulo.play()

class DinoVoador(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet, escolha):

        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []

        for i in range(3, 5):
            img = sprite_sheet.subsurface((i*32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*2, 32*2))
            self.imagens_dinossauro.append(img)

        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA, 300)
        self.rect.x = LARGURA
        self.velocidade = 10

    def update(self):

        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = LARGURA
            self.rect.x -= self.velocidade

            if self.index_lista >= 1:
                self.index_lista = 0 
            self.index_lista += 0.25
            self.image = self.imagens_dinossauro[int(self.index_lista)] #atualizando a imagem do dino voador

