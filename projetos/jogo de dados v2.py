import pygame
from random import randint 
from itertools import cycle 
from pygame.locals import *

pygame.init()
dInfo = pygame.display.Info()
tela = pygame.display.set_mode((dInfo.current_w, dInfo.current_h), pygame.FULLSCREEN) 
loop = True
atualizar = True
corFundo = cycle([(20, 20, 20), (25, 25, 25)]) 
corFonte = (255, 255, 255)
fonte = pygame.font.SysFont("serif", int(10 * tela.get_width() / 100)) 
valor = fonte.render("clique na tela", 1, corFonte)
fps = pygame.time.Clock()
  
while loop:
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      pygame.quit()
      exit()
    if evento.type == pygame.MOUSEBUTTONDOWN:
      valor = fonte.render(f"valor: {randint(1, 6)}", 1, corFonte)
      atualizar = True
  if atualizar:
    tela.fill(next(corFundo))
    tela.blit(valor, (tela.get_width() / 2 - valor.get_width() / 2, tela.get_height() / 2 - valor.get_height() / 2))
    pygame.display.flip()
    atualizar = False
  fps.tick(20)
