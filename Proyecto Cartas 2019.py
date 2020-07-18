#Juego Cartas
import pygame, sys,datetime,time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((960, 600)) # se define la resolucion de pantalla ( en este caso es la mitad de Full HD ).

# se definen los colores
BLUE = ( 0, 0, 255)
DARKORANGE = (255,140,0)
GOLD = (255,215,0)
ORANGERED =(255,69,0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = ( 255,255,255 )


fontObj = pygame.font.Font('freesansbold.ttf', 16)

DISPLAYSURF.fill(WHITE) # se llena la pantalla de color azul por defecto

FPS = 60 #se define la velocidad en frames del juego
fpsClock = pygame.time.Clock()

#Coordenadas declaradas que luego se van a modificar en el bucle

manoX=500
manoY=460
minutos = 00
mil = 0

animX=500
animY=460

animX2=500
animY2=460

animX3=500
animY3=460

animX4=500
animY4=460

animX5=500
animY5=460

animX6=500
animY6=460

animXB=500
animYB=10

animX2B=500
animY2B=10

animX3B=500
animY3B=10

animX4B=500
animY4B=10

animX5B=500
animY5B=10

animX6B=500
animY6B=10

starting_point = time.time()
no = 0

pygame.display.set_caption('Proyecto Cartas 2019') # texto que aparecera en la ventana del juego
while True: # BUCLE PRINCIPAL DEL JUEGO : corre cada segundo
        t = datetime.datetime.now().hour
        actual = str(t)

        t2 = datetime.datetime.now().minute
        actual2 = str(t2)

        t3 = datetime.datetime.now().second
        actual3 = str(t3)

        elapsed_time = time.time () - starting_point
        elapsed_time_int = int(elapsed_time)
        elapsed_time_minutes = elapsed_time_int / 60
        elapsed_time_seconds = elapsed_time_int % 60
        ea = str(elapsed_time_minutes)
        ei = str(elapsed_time_seconds)
        
        #Para cargar los graficos luego
        ranura = pygame.image.load('ranura.png')
        ranura2 = pygame.image.load('ranura2.png')
        ranura3 = pygame.image.load('ranura3.png')
        mano = pygame.image.load('mano.png')
        generica = pygame.image.load('generica.png')
        genericaB = pygame.image.load('genericaB.png')
        ranuraB = pygame.image.load('ranuraB.png')
        detalle = pygame.image.load('detalle.png')
        cuadro = pygame.image.load('cuadro.png')
        jugador = pygame.image.load('personaje1.png')
        jugador2 = pygame.image.load('personaje2.png')
        ranura2B = pygame.image.load('ranura2B.png')
        ranura3B = pygame.image.load('ranura3B.png')
        dado = pygame.image.load('dado1.png')
        dado2 = pygame.image.load('dado2.png')
        dado3 = pygame.image.load('dado3.png')
        dado4 = pygame.image.load('dado4.png')
        dado5 = pygame.image.load('dado5.png')
        dado6 = pygame.image.load('dado6.png')
        fondo = pygame.image.load('fondo2.png')
        c1 = pygame.image.load('c1.png')
        c2 = pygame.image.load('c2.png')
        c3 = pygame.image.load('c3.png')
        c4 = pygame.image.load('c4.png')
        c5 = pygame.image.load('c5.png')
        c6 = pygame.image.load('c6.png')
        c7 = pygame.image.load('c7.png')
        c8 = pygame.image.load('c8.png')
        c9 = pygame.image.load('c9.png')
        c10 = pygame.image.load('c10.png')
        c11 = pygame.image.load('c11.png')
        c12 = pygame.image.load('c12.png')
        c13 = pygame.image.load('c13.png')
        c14 = pygame.image.load('c14.png')
        c15 = pygame.image.load('c15.png')
        

        #se carga la imagen del personaje,se le define un color de transparencia y se carga en pantalla junto a sus coordenadas
        ranura.set_colorkey(WHITE)
        ranura2.set_colorkey(WHITE)
        ranura3.set_colorkey(WHITE)

        ranuraB.set_colorkey(WHITE)
        ranura2B.set_colorkey(WHITE)
        ranura3B.set_colorkey(WHITE)
        mano.set_colorkey(WHITE)
        generica.set_colorkey(WHITE)
        genericaB.set_colorkey(WHITE)
        DISPLAYSURF.blit(fondo, (0, 0))
        DISPLAYSURF.blit(ranura3B, (50, 10))
        DISPLAYSURF.blit(ranura3B, (200, 10))
        DISPLAYSURF.blit(ranura3B, (350, 10))
        DISPLAYSURF.blit(ranura2B, (500, 10))

        DISPLAYSURF.blit(ranuraB, (50, 160))
        DISPLAYSURF.blit(ranuraB, (200, 160))
        DISPLAYSURF.blit(ranuraB, (350, 160))
        
        DISPLAYSURF.blit(ranura, (50, 310))
        DISPLAYSURF.blit(ranura, (200, 310))
        DISPLAYSURF.blit(ranura, (350, 310))
        
        DISPLAYSURF.blit(ranura3, (50, 460))
        DISPLAYSURF.blit(ranura3, (200, 460))
        DISPLAYSURF.blit(ranura3, (350, 460))
        DISPLAYSURF.blit(ranura2, (500, 460))
        
        DISPLAYSURF.blit(jugador, (700, 10))
        DISPLAYSURF.blit(jugador2, (830, 10))
        #DISPLAYSURF.blit(detalle, (700, 110))
        #DISPLAYSURF.blit(cuadro, (700, 380))


        if(animX>50):
                animX-=30

        if(animX2>200):
                animX2-=20

        if(animX3>350):
                animX3-=10
                

        if(animXB>50):
                animXB-=30

        if(animX2B>200):
                animX2B-=20

        if(animX3B>350):
                animX3B-=10
                

        if(animY>310 and animX==50):
                animY-=10

        if(animY2>310 and animX2==200):
                animY2-=10

        if(animY3>310 and animX3==350):
                animY3-=10

        if(animYB<160 and animXB==50):
                animYB+=10

        if(animY2B<160 and animX2B==200):
                animY2B+=10

        if(animY3B<160 and animX3B==350):
                animY3B+=10

        if(animX==50 and animY==310 ):
                if(animX4>50):
                        animX4-=30

        if(animX2==200 and animY2==310 ):
                if(animX5>200):
                        animX5-=20

        if(animX3==350 and animY3==310 ):
                if(animX6>350):
                        animX6-=10

        DISPLAYSURF.blit(c1, (animX3, animY3))
        DISPLAYSURF.blit(c2, (animX2, animY2))
        DISPLAYSURF.blit(c3, (animX, animY))
        DISPLAYSURF.blit(c4, (animX4, animY4))
        DISPLAYSURF.blit(c5, (animX5, animY5))
        DISPLAYSURF.blit(c6, (animX6, animY6))

        DISPLAYSURF.blit(c7, (animXB,animYB))
        DISPLAYSURF.blit(c8, (animX2B,animY2B))
        DISPLAYSURF.blit(c9, (animX3B,animY3B))
        DISPLAYSURF.blit(c10, (animX4B,animY4B))
        
        #no+=1
        #if(no==1):
                #DISPLAYSURF.blit(dado, (500,310))
        #if(no==3):
                #DISPLAYSURF.blit(dado2, (500,310))
        #if(no==5):
                #DISPLAYSURF.blit(dado3, (500,310))
        #if(no==7):
                #DISPLAYSURF.blit(dado4, (500,310))
        #if(no==9):
                #DISPLAYSURF.blit(dado5, (500,310))
        #if(no==11):
                #DISPLAYSURF.blit(dado6, (500,310))
                #no=0

        DISPLAYSURF.blit(mano, (manoX, manoY))

        hora = fontObj.render("Hora: "+actual+":"+actual2+":"+actual3,True,BLACK,WHITE)
        horaR = hora.get_rect()
        horaR.center = (0, 0)

        hora2 = fontObj.render(ea+":"+ei,True,BLUE,WHITE)
        horaR2 = hora.get_rect()
        horaR2.center = (0, 0)

        DISPLAYSURF.blit(hora, (690, 570))
        DISPLAYSURF.blit(hora2, (690, 540))
        for event in pygame.event.get():

                if event.type == pygame.KEYUP : #si x tecla no esta pulsada,el valor del boton sera 0 ( no pulsado ).
                    if event.key == pygame.K_LEFT :
                            manoX-=150
                    elif event.key == pygame.K_RIGHT :
                            manoX+=150
                    elif event.key == pygame.K_UP :
                            manoY-=150
                    elif event.key == pygame.K_DOWN :
                            manoY+=150

                if(manoX<50):
                        manoX=50
                if(manoX>500):
                        manoX=500
                
                if(manoY<10):
                        manoY=10
                if(manoY>460):
                        manoY=460

                elif event.type == QUIT: #si se pulsa esc,se sale del juego
                        pygame.quit()
                        sys.exit()

        pygame.display.update() # se actualiza la pantalla cada segundo
