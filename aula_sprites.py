import pygame
from pygame.locals import *
from sys import exit
from sapo import Sapo
from personagem import Personagem

pygame.init()

largura = 640
altura = 480
PRETO = (0,0,0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')
relogio = pygame.time.Clock()

todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
personagem = Personagem()
todas_as_sprites.add(personagem)

imagem_fundo = pygame.image.load("cidade_fundo.jpg").convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

while True:

    tela.fill(PRETO)
    relogio.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()

    tela.blit(imagem_fundo, (0,0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()