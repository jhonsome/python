import pygame 
from pygame.locals import *
from plyer import flash 
pygame.init()

TELA = pygame.display.set_mode()
FPS = pygame.time.Clock()

flash.on()
while True:
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      flash.off()
      pygame.quit()
      exit()
    elif evento.type == pygame.MOUSEBUTTONDOWN:
      flash.off()
    elif evento.type == pygame.MOUSEBUTTONUP:
      flash.on()
  TELA.fill((20, 20, 20))
  pygame.display.flip()
  FPS.tick(60)
