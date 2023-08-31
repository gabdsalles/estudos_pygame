import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.font.init()
pygame.mixer.init()

LARGURA = 640
ALTURA = 480
x = LARGURA / 2
y = ALTURA / 2
x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont("comic sans ms", 30, True, True)

musica_de_fundo = pygame.mixer.music.load("BoxCat Games - CPU Talk.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav') #tem que ser wav, apenas a musica de fundo é mp3

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))

clock = pygame.time.Clock()  # Create a clock object to control frame rate

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        mensagem = f'Pontos: {pontos}'
        texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] or keys[K_d]:
            x += 20
        if keys[K_LEFT] or keys[K_a]:
            x -= 20
        if keys[K_UP] or keys [K_w]:
            y -= 20
        if keys[K_DOWN] or keys [K_s]:
            y += 20

    tela.fill((0, 0, 0))

    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 60))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 60))

    if ret_vermelho.colliderect(ret_azul):
        # print("Colidiu!")
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        ret_azul.x = x_azul
        ret_azul.y = y_azul
        pontos += 1
        barulho_colisao.play()
        


    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()

    clock.tick(60)  # Control frame rate to 60 FPS
