import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

tela = pygame.display.set_mode((400, 700), pygame.FULLSCREEN | pygame.SCALED)
telaLargura, telaAltura = tela.get_width(), tela.get_height()
fps = pygame.time.Clock()

  
class Imagem(object):
    
  def __init__(self, posX, posY, largura, altura, imagem):
    if type(imagem) == pygame.Surface:
      self.img = pygame.Surface((largura, altura))
      self.S = True
    else:
      self.imgOriginal = pygame.image.load(imagem)
      self.img = pygame.transform.smoothscale(self.imgOriginal, (largura, altura))
      self.S = False
    self.ret = pygame.Rect(posX, posY, largura, altura)
    self.pos = (posX, posY)
    self.tam = (largura, altura)
    
    
  def exibirImagem(self, superfície, RGBA = None):
    if self.S:
      if RGBA != None:
        self.img.fill(RGBA)
      else:
        self.img.fill((20, 20, 20))
    superfície.blit(self.img, self.ret)
    
    
  def moverImagem(self, X, Y):
    self.ret = self.ret.move(X, Y)
    
    
  def redimensionar(self, posX, posY, largura, altura):
    self.img = pygame.transform.smoothscale(self.imgOriginal, (largura, altura))
    self.ret = pygame.Rect(posX, posY, largura, altura)
    
    
  def retornarRet(self):
    return self.ret
    
  
class Botão(object):
    
  def __init__(self, posX, posY, largura, altura, botãoLivre = None, botãoPressionado = None, som = None):
    if botãoLivre == None:
      botão01 = None
    elif type(botãoLivre) == pygame.Surface:
      botão01 = pygame.Surface((largura, altura))
      self.S1 = True
    else:
      botão01 = pygame.transform.smoothscale(pygame.image.load(botãoLivre), (int(largura), int(altura)))
    if botãoPressionado == None:
      botão02 = None
    elif type(botãoPressionado) == pygame.Surface:
      botão02 = pygame.Surface((largura, altura))
      self.S2 = True
    else:
      botão02 = pygame.transform.smoothscale(pygame.image.load(botãoPressionado),  (int(largura), int(altura)))
    if som != None:
      som = pygame.mixer.Sound(som)
      self.som = som
    self.img = (botão01, botão02)
    self.b = 0
    self.ret = pygame.Rect(posX, posY, largura, altura)
      
      
  def exibirBotao(self, superfície, RGBA = None):
    if self.img[0] != None:
      if self.b == 0:
        if self.S1:
          if RGBA != None:
            self.img[0].fill(RGBA)
          else:
            self.img[0].fill((20, 20, 20))
        superfície.blit(self.img[0], self.ret)
    if self.img[1] != None:
      if self.b == 1:
        if self.S2:
          if RGBA != None:
            self.img[1].fill(RGBA)
          else:
            self.img[1].fill((20, 20, 20))
        superfície.blit(self.img[1], self.ret)
        
        
  def Clique(self, eventos, tipo = 0):
    if eventos.type == pygame.MOUSEBUTTONDOWN:
      t1 = pygame.mouse.get_pos()
      if t1[0] > self.ret.left and t1[0] < self.ret.right and t1[1] > self.ret.top and t1[1] < self.ret.bottom:
        self.t = True
        self.b = 1
        if tipo == 0:
          return True
        if tipo == 1:
          return False
      else:
        self.t = False
    if eventos.type == pygame.MOUSEBUTTONUP:
      try:
        if self.t == True:
          self.t = False
          self.b = 0
          t2 = pygame.mouse.get_pos()
          if t2[0] > self.ret.left and t2[0] < self.ret.right and t2[1] > self.ret.top and t2[1] < self.ret.bottom:
            if self.som != None:
              self.som.play(maxtime = 1000)
              self.som.fadeout(2000)
            if tipo == 0:
              return False
            if tipo == 1:
              return True
      except AttributeError:
        self.t = False


 


def intro():
  loop = True
  fonte = pygame.font.SysFont("Arial", 22)
  texto1 = fonte.render("           PONG", 1, (200, 200, 200)) 
  texto2 = fonte.render("Não encoste a raquete nos", 1, (200, 200, 200))
  texto3 = fonte.render("  cantos da parede.", 1, (200, 200, 200)) 
  texto4 = fonte.render("Não deixe o quadrado cair.", 1, (200, 200, 200))
  texto5 = fonte.render("boa sorte!", 1, (200, 200, 200)) 
  textos = [texto1, texto2, texto3, texto4, texto5]
  txtb1 = fonte.render("lado direito da tela: botão direito", 1, (200, 200, 200))
  txtb2 = fonte.render("lado esquerdo da tela: botão esquerdo", 1, (200, 200, 200))
  continuar = fonte.render("Clique para continuar.", 1, (0, 255, 0))
  while loop:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT or evento.type == pygame.MOUSEBUTTONDOWN:
        loop = False
      
    num = 10
    tela.fill((20, 20, 20))
    for texto in textos:
      tela.blit(texto, (10, num))
      num += 24
    tela.blit(txtb1, (0, 350))
    tela.blit(txtb2, (0, 374))
    tela.blit(continuar, (90, 470))
    pygame.display.flip()
    fps.tick(30)


def perdeu():
  loop = True
  fonte = pygame.font.SysFont("Arial", 27)
  Label1 = fonte.render("Você perdeu!", 1, (255, 0, 0))
  Label2 = fonte.render("Clique para continuar.", 1, (255, 255, 255))
  
  while loop:
    tela.blit(Label1, (113, 300))
    tela.blit(Label2, (70, 380))
    pygame.display.flip()
    fps.tick(30)
    
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        loop = False
      if evento.type == pygame.MOUSEBUTTONDOWN:
        loop = False
    

def jogo(jogadas, tempo, melhorRodada):
  fonte = pygame.font.SysFont("Arial", 16)
  melhorTempo = fonte.render(f"melhor tempo (milissegundos): {tempo:.3f} rodada: {melhorRodada}", 1, (0, 0, 0))
  txtJogadas = fonte.render(f"{jogadas}° rodada", 1, (0, 0, 0))
  tabela = Imagem(0, 0, telaLargura, 60, pygame.Surface((0, 0)))
  linha = Imagem(0, 90, telaLargura, 2, pygame.Surface((0, 0)))
  linha2 = Imagem(0, 90, 2, 20, pygame.Surface((0, 0)))
  linha3 = Imagem(telaLargura - 2, 90, 2, 20, pygame.Surface((0, 0)))
  bola = Imagem(randint(0, 269), randint(400, 500), 30, 30, pygame.Surface((0, 0)))
  barra = Imagem(140, 90, 38, 10, pygame.Surface((0, 0)))
  b1 = Botão(0, 0, telaLargura / 2, telaAltura)
  b2 = Botão((telaLargura / 2) - 1, 0, telaLargura / 2, telaAltura)
  vel = 8
  t = False
  velX = 10
  velY = velX - 2
  time = 0
  cor = (255, 255, 255)
  
  while True:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        break
      if evento.type == pygame.MOUSEBUTTONDOWN:
        if b2.Clique(evento) == True:
          vel = abs(vel)
          t = True
        if b1.Clique(evento) == True:
          if vel > 0:
            vel = -vel
          t = True
      if evento.type == pygame.MOUSEBUTTONUP:
        t = False
        
    if t == True:
      barra.moverImagem(vel, 0)
    
    bola.moverImagem(velX, velY)
    
    if bola.retornarRet().left < 0 or bola.retornarRet().right > telaLargura:
      velX = -velX
    if bola.retornarRet().bottom > telaAltura or bola.retornarRet().colliderect(barra.retornarRet()):
      velY = -velY
      cor = (randint(0, 255), randint(0, 255), randint(0, 255))
    
    time += 0.03
    
    tela.fill((20, 20, 20))
    tabela.exibirImagem(tela, (255, 255, 255))
    tela.blit(txtJogadas, (0, 0))
    tempoAtual = fonte.render(f"tempo atual (milissegundos): {time:.3f}", 1, (0, 0, 0))
    tela.blit(tempoAtual, (0, 20))
    tela.blit(melhorTempo, (0, 40))
    linha.exibirImagem(tela, (255, 0, 0))
    linha2.exibirImagem(tela, (255, 0, 0))
    linha3.exibirImagem(tela, (255, 0, 0))
    bola.exibirImagem(tela, cor)
    barra.exibirImagem(tela, (255, 255, 255))
    pygame.display.flip()
    fps.tick(30)
    
    if bola.retornarRet().top < linha.retornarRet().bottom or barra.retornarRet().left < linha2.retornarRet().right or barra.retornarRet().right > linha3.retornarRet().left:
      return time
    

    
rodada = 1
melhorRodada = "–"
melhorTempo = 0
intro()
while True:
  print(type(pygame.Rect(0, 0, 100, 100)))
  t = jogo(rodada, melhorTempo, melhorRodada)
  if t > melhorTempo:
    melhorTempo = t
    melhorRodada = rodada
  perdeu()
  rodada += 1
 