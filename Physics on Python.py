# -*- coding: utf-8 -*-
"""
Physics on Python
"""

# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
import time
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'imagens')

# Dados gerais do jogo.
WIDTH = 720 # Largura da tela
HEIGHT = 480 # Altura da tela
FPS = 60 # Frames por segundo

g = 10
# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TRANSPARENTE = (200,0,200)
# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, player_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 50))
        
        # Deixando transparente.
        self.image.set_colorkey(TRANSPARENTE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        
        # Velocidade da nave
        self.speedx = 0
        self.speedy = 0
        # Esfera saltando:
        self.jumping = False
        self.jumpingCount = 0
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
    
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        else:
            self.jumping = False
            self.jumpingCount += 1
            self.speedy += 3
                    
            
            
# Carrega todos os assets uma vez só.
def load_assets(img_dir):
    assets = {}
    assets["player_img"] = pygame.image.load(path.join(img_dir, "Esfera.png")).convert()
    img = pygame.image.load(path.join(img_dir, "background.png")).convert()
    img.set_colorkey(TRANSPARENTE)
    assets["background"] = img
    img = pygame.image.load(path.join(img_dir, "floor.png")).convert()
    img.set_colorkey(TRANSPARENTE)
    assets["floor"] = img
    
    return assets

def game_screen(screen):
    # Carrega todos os assets uma vez só e guarda em um dicionário
    assets = load_assets(img_dir)

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    background = assets["background"]
    background_rect = background.get_rect()
    
    # Carrega o chão do jogo
    floor = assets["floor"]
    floor_rect = floor.get_rect()
    floor_rect.bottom = HEIGHT


    # Cria uma esfera. O construtor será chamado automaticamente.
    player = Player(assets["player_img"])

    # Cria um grupo de todos os sprites e adiciona a nave.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    PLAYING = 0
    DONE = 2
    state = PLAYING
    while state != DONE:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        if state == PLAYING:
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE
                
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = -8
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 8
                    if not player.jumping:
                        if event.key == pygame.K_UP:
                            player.speedy = -30
                        if event.key == pygame.K_DOWN:
                            player.speedy = 8
                    if event.key == pygame.K_SPACE:
                        player.jumping = True
                        player.update()
                        
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    if event.key == pygame.K_UP:
                        player.jumpingCount = 0
                        player.speedy = 0
                    if event.key == pygame.K_DOWN:
                        player.speedy = 0
                    if event.key == pygame.K_SPACE:
                        player.jumping = False
                        player.update()
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        screen.blit(floor,floor_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

# Inicialização do Pygame.
pygame.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Bola")

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
