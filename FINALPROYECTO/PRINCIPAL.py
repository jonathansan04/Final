import sys, pygame, UTIL
from pygame.locals import *
from NAVE import *
from ASTEROIDE import *



SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
ICON_SIZE = 32

def game():
      pygame.init()
      pygame.mixer.init()
      screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
      jugando = True
      pygame.display.set_caption("Galaxy" )
      fuente = pygame.font.Font(None, 30)
      background_image = UTIL.cargar_imagen('Imagenes/fondo.jpg');
      pierde_vida = UTIL.cargar_sonido('Sonidos/el-pollo_1.mp3')
      #gana_punt = UTIL.cargar_sonido('Sonidos/misc108.mp3')
      pygame.mouse.set_visible( False )
      temporizador = pygame.time.Clock()
      NAVE = Nave()
      ASTEROIDE = [Asteroide((0,40),6),Asteroide((0,0),6),Asteroide((50,100),4),Asteroide((100,200),10),Asteroide((150,300),8),Asteroide((200,70),20),Asteroide((200,50),20)]
      while jugando:
          NAVE.update()
          if NAVE.vida <= 0:
              jugando = False
          texto_vida = fuente.render("Vida: " + str(NAVE.vida), 1, (250, 250, 250))
          for n in ASTEROIDE:
              n.update()
          NAVE.image = NAVE.imagenes[0]
          for n in ASTEROIDE:
              if NAVE.rect.colliderect(n.rect):
                  NAVE.image = NAVE.imagenes[1]
                  pierde_vida.play()
                  NAVE.vida -= 1
              
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()
          screen.blit(background_image, (0,0))
          screen.blit(NAVE.image, NAVE.rect)
          for n in ASTEROIDE:
              screen.blit(n.image, n.rect)
          screen.blit(texto_vida, (20, 10))
          pygame.display.update()
          pygame.time.delay(10)
          texto_vida = fuente.render("Puntaje: " + str(NAVE.punt), 1, (250, 250, 250))
          screen.blit(texto_vida, (400, 10))
          pygame.display.update()
          pygame.time.delay(10)
        
                
         
   
if __name__ == '__main__':
      game()
