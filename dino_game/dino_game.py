import pygame
import os
from pygame.locals import *
from sys import exit
from sprites import Dino, Chao, Cacto, Nuvens, DinoVoador
from random import choice

LARGURA = 640
ALTURA = 480

pygame.init()
pygame.mixer.init()
pygame.font.init()

pontos = 0
velocidade_jogo = 10

def exibe_mensagem(msg, tamanho, cor):

    fonte = pygame.font.SysFont("comic sans ms", tamanho, True, True)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

def reiniciar_jogo():

    global pontos, velocidade_jogo, colidiu, escolha_obstaculo

    pontos = 0
    velocidade_jogo = 10
    colidiu = False

    dino_voador.rect.x = LARGURA
    cacto.rect.x = LARGURA
    escolha_obstaculo = choice([0, 1])
    dino.rect.y = dino.posY_inicial
    dino.pulo = False



diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

tela = pygame.display.set_mode((LARGURA, ALTURA))
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'dinoSpritesheet.png')).convert_alpha()
pygame.display.set_caption('Dino Game')

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'death_sound.wav'))
som_colisao.set_volume(1)

colidiu = False
escolha_obstaculo = choice([0, 1])

som_pontuacao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'score_sound.wav'))
som_pontuacao.set_volume(1)

todas_as_sprites = pygame.sprite.Group()
dino_and_chao_sprite = pygame.sprite.Group()
dino = Dino(sprite_sheet, diretorio_sons)
dino_and_chao_sprite.add(dino)
x_pos = 0

for i in range(4):

    nuvem = Nuvens(sprite_sheet)
    todas_as_sprites.add(nuvem)

for i in range(20):

    chao = Chao(sprite_sheet, x_pos)
    dino_and_chao_sprite.add(chao)
    x_pos += 64

cacto = Cacto(sprite_sheet, escolha_obstaculo)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto)
todas_as_sprites.add(cacto)

dino_voador = DinoVoador(sprite_sheet, escolha_obstaculo)
todas_as_sprites.add(dino_voador)
grupo_obstaculos.add(dino_voador)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE and colidiu == False:
                if dino.rect.y != dino.posY_inicial:
                    pass
                else:
                    dino.pula()
            
            if event.key == K_r and colidiu == True:

                reiniciar_jogo()
        
    colisoes = pygame.sprite.spritecollide(dino, grupo_obstaculos, False, pygame.sprite.collide_mask)
    todas_as_sprites.draw(tela)
    dino_and_chao_sprite.draw(tela)

    if dino_voador.rect.topright[0] < 0 or cacto.rect.topright[0] < 0:
        
        escolha_obstaculo = choice([0, 1])
        cacto.escolha = escolha_obstaculo
        dino_voador.escolha = escolha_obstaculo
        cacto.rect.x = LARGURA
        dino_voador.rect.x = LARGURA
        
    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True

    if colidiu == True:
        if pontos % 100 == 0:
            pontos += 1
        
        texto_game_over = exibe_mensagem('Game Over', 40, PRETO)
        texto_instrucao_reiniciar = exibe_mensagem('Pressione r para reiniciar', 20, PRETO)
        tela.blit(texto_game_over, (LARGURA//2, ALTURA//2))
        tela.blit(texto_instrucao_reiniciar, (LARGURA//2, ALTURA//2 + 50))
    else:
        pontos += 1
        dino_and_chao_sprite.update()
        todas_as_sprites.update()
        texto_pontuacao = exibe_mensagem(pontos, 40, PRETO)

    if pontos % 100 == 0:
        som_pontuacao.play()
        if velocidade_jogo >= 30:
            velocidade_jogo += 0
        else:
            velocidade_jogo += 1
        for sprite in todas_as_sprites:
            sprite.velocidade = velocidade_jogo

    tela.blit(texto_pontuacao, (LARGURA - 120, 40))
    pygame.display.flip()