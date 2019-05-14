"""
pyg4m3.game
"""
import pygame
pygame.init()

pygame.display.set_caption("Tela inicial")

#Parâmetros da página do jogo
JANELA = pygame.display.set_mode((720,480))
LARGURA = 720
ALTURA = 480
x,y = LARGURA/2,ALTURA/2
L = 50
H = 50
V = 20
# CORES:
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

running = True
while running:        # Loop principal
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x >= V:
            x -= V
    if keys[pygame.K_RIGHT]:
        if x + V + L >= LARGURA:
            x = LARGURA - L 
        else:
            x += V
    if keys[pygame.K_UP]:
        if y > V:
            y -= V
    if keys[pygame.K_DOWN]:
        if y + V <= ALTURA:
            y += V
        
    JANELA.fill(BLACK)

    pygame.draw.rect(JANELA, RED,  (x, y, 50, 50))
    pygame.display.update()
pygame.quit() 