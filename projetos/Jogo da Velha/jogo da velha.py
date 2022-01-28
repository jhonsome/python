import pygame 
from pygame.locals import * 
from random import randint 
pygame.init()

LARGURATELA, ALTURATELA = pygame.display.Info().current_w, pygame.display.Info().current_h
TELA = pygame.display.set_mode((LARGURATELA, ALTURATELA), pygame.FULLSCREEN | pygame.SCALED)
FONTE = pygame.font.SysFont("arial", int(15 * TELA.get_width() / 100))
FPS = pygame.time.Clock()
MÍDIAS = (
  "mídias/imagens/fundo.png", 
  "mídias/imagens/tile.png", 
  "mídias/imagens/botão fundo.png", 
  "mídias/imagens/placar.png", 
)
IMAGENS = dict()
SONS = dict()
RETÂNGULOS = dict()

def Porcentagem(p, v):
  """
  Retorna a porcentagem de um valor
  
  p: porcento
  v: valor
  """
  return p * v / 100

def CarregarImg(img, resolução):
  """
  Retorna uma pygame.Surface redimensionada
  
  img: string com o caminho do arquivo de imagem
  resolução: um iterável com os valores de largura e altura
  """
  resolução = (int(resolução[0]), int(resolução[1])) 
  return pygame.transform.smoothscale(pygame.image.load(img), resolução).convert_alpha()

def CarregarTxt(txt, resolução, cor = (255, 255, 255)):
  """
  Retorna uma pygame.Surface redimensionada com um texto 
  
  txt: string com um texto qualquer
  resolução: um iterável com os valores de largura e altura
  cor: cor do texto
  """
  resolução = (int(resolução[0]), int(resolução[1]))
  return pygame.transform.smoothscale(FONTE.render(txt, True, cor), resolução).convert_alpha()

def _Jogo():
  jogadorAtual = randint(0, 1)
  tabuleiro = [[None for n in range(3)] for n in range(3)]
  jogador1X = margem * 2
  jogador1Y = margem * 2
  jogador1Pontos = 0
  jogador2X = Porcentagem(60, LARGURATELA)
  jogador2Y = margem * 2
  jogador2Pontos = 0
  jogadorAtualX = margem 
  jogadorAtualY = (tileTam + margem) * 3 + margem + (Porcentagem(10, LARGURATELA) + margem)
  IMAGENS["jogador atual"] = CarregarTxt(f"Vez do jogador {'X' if jogadorAtual == 0 else 'Y'}", (Porcentagem(100, LARGURATELA), Porcentagem(15, ALTURATELA))) 
  while True:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        pygame.quit()
        exit()
      elif evento.type == pygame.MOUSEBUTTONDOWN:
        for l in range(len(RETÂNGULOS["tiles"])):
          for a in range(len(RETÂNGULOS["tiles"][l])):
            if RETÂNGULOS["tiles"][l][a].collidepoint(evento.pos):
              if smbLista[l][a] == None:
                tebuleiro[l][a] = jogadorAtual
                jogadorAtual = 0 if smbAtual == 1 else 1
    TELA.blit(IMAGENS["fundo"], (0, 0))
    TELA.blit(IMAGENS["placar"], (margem, margem))
    TELA.blit(IMAGENS["placar X"], (jogador1X, jogador1Y))
    TELA.blit(IMAGENS["placar O"], (jogador2X, jogador2Y))
    for l in range(len(RETÂNGULOS["tiles"])):
      for a in range(len(RETÂNGULOS["tiles"][l])):
        TELA.blit(IMAGENS["tile"], RETÂNGULOS["tiles"][l][a])
        if tabuleiro[l][a] != None:
          TELA.blit(smbLista[l][a], RETÂNGULOS["tiles"][l][a])
    TELA.blit(IMAGENS["jogador atual"], (jogadorAtualX, jogadorAtualY))
    pygame.display.update()
    FPS.tick(fps)
        
def _FimJogo(pontuação):
  pass

def _Início():
  global fps, margem, tileTam
  fps = 30
  tileTam = Porcentagem(33.3, LARGURATELA)
  margem = Porcentagem(1, LARGURATELA)
  botãoJogarX = Porcentagem(25, LARGURATELA) + margem
  botãoJogarY = Porcentagem(40, ALTURATELA) + margem 
  botãoSairX = Porcentagem(25, LARGURATELA) + margem
  botãoSairY = Porcentagem(50, ALTURATELA) + margem 
  IMAGENS["fundo"] = CarregarImg(MÍDIAS[0], (LARGURATELA, ALTURATELA))
  IMAGENS["botão fundo"] = CarregarImg(MÍDIAS[2], (Porcentagem(50, LARGURATELA) - margem * 2, Porcentagem(10, ALTURATELA) - margem * 2)) 
  IMAGENS["botão jogar"] = CarregarTxt("Jogar", (Porcentagem(50, LARGURATELA) - margem * 2, Porcentagem(10, ALTURATELA) - margem * 2))
  IMAGENS["botão sair"] = CarregarTxt("Sair", (Porcentagem(50, LARGURATELA) - margem * 2, Porcentagem(10, ALTURATELA) - margem * 2))
  IMAGENS["tile"] = CarregarImg(MÍDIAS[1], (tileTam - margem * 2, tileTam - margem * 2))
  IMAGENS["placar"] = CarregarImg(MÍDIAS[3], (Porcentagem(100, LARGURATELA) - margem * 2, Porcentagem(10, ALTURATELA) - margem * 2))
  IMAGENS["x"] = CarregarTxt("X", (tileTam - margem * 2, tileTam - margem * 2)) 
  IMAGENS["o"] = CarregarTxt("O", (tileTam - margem * 2, tileTam - margem * 2))
  IMAGENS["placar X"] = CarregarTxt("p: 0 - X", (Porcentagem(40, LARGURATELA) - margem * 2, Porcentagem(10, ALTURATELA) - margem * 2))
  IMAGENS["placar O"] = CarregarTxt(f"O - p: 0", (Porcentagem(40, LARGURATELA) - margem * 2, Porcentagem(10, ALTURATELA) - margem * 2))
  RETÂNGULOS["tiles"] = [[pygame.Rect(tileTam * l + margem, Porcentagem(10, ALTURATELA) + tileTam * a + margem, tileTam - margem * 2, tileTam - margem * 2) for a in range(3)] for l in range(3)]
  RETÂNGULOS["botão jogar"] = pygame.Rect((botãoJogarX, botãoJogarY), IMAGENS["botão jogar"].get_size())
  RETÂNGULOS["botão sair"] = pygame.Rect((botãoSairX, botãoSairY), IMAGENS["botão sair"].get_size())
  while True:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        pygame.quit()
        exit()
      elif evento.type == pygame.MOUSEBUTTONDOWN:
        if RETÂNGULOS["botão jogar"].collidepoint(evento.pos):
          pontos = _Jogo()
        elif RETÂNGULOS["botão sair"].collidepoint(evento.pos):
          pygame.quit()
          exit()
    TELA.blit(IMAGENS["fundo"], (0, 0))
    TELA.blit(IMAGENS["botão fundo"], RETÂNGULOS["botão jogar"])
    TELA.blit(IMAGENS["botão fundo"], RETÂNGULOS["botão sair"])
    TELA.blit(IMAGENS["botão jogar"], RETÂNGULOS["botão jogar"])
    TELA.blit(IMAGENS["botão sair"], RETÂNGULOS["botão sair"])
    pygame.display.update()
    FPS.tick(fps)

if __name__ == "__main__":
  _Início()
