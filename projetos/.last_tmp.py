import pygame 
from pygame.locals import *
from plyer import accelerometer
pygame.init()

TELA = pygame.display.set_mode()
FONTE = pygame.font.SysFont("serif", 20)
FPS = pygame.time.Clock()

def _início():
  accelerometer.enable()
  fpsTick = 60
  loop = True
  while loop:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        pygame.quit()
        exit()
    x, y, z = accelerometer.acceleration
    txt = FONTE.render(f"x: {x:.2f}, y: {y:.2f}, z: {z:.2f}", True, (255, 255, 255))
    TELA.fill((20, 20, 20))
    TELA.blit(txt, (0, 0))
    pygame.display.flip()
    FPS.tick(fpsTick)

if __name__ == "__main__":
  _início()