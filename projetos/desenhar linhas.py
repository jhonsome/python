import pygame 
from pygame.locals import * 
pygame.init()

TELA = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.FULLSCREEN | pygame.SCALED)
FPS = pygame.time.Clock()

def _início():
  pontos = list()
  larguraLinha = 1
  corLinha = (255, 255, 255)
  while True:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        return None
      elif evento.type == pygame.MOUSEBUTTONDOWN:
        pontos.append(evento.pos)
    TELA.fill((20, 20, 20))
    if len(pontos) > 1:
      for p in range(len(pontos) - 1):
        pygame.draw.line(TELA, corLinha, pontos[p], pontos[p + 1], larguraLinha)
    pygame.display.flip()
    FPS.tick(60)

if __name__ == "__main__":
  _início()
  pygame.quit()
  exit()
