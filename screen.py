import sys, os

# Disable print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Enable print
def enablePrint():
    sys.stdout = sys.__stdout__


blockPrint()
import pygame
enablePrint()


if len(sys.argv) <2:
    print(" Debes ingresar:")
    print(" Timer_Minutos Timer_Segundos  Alarma_segundos")
    print(" Ejemplo para 1 minuto 30 segundos y alarma 20 segundos")
    print(" python screen.py -m 01 -s 30 -a 20")
    exit()
alarma = 20
minutos = 0
segundo = 0

for idx, arg in enumerate(sys.argv):
    if arg in ('-m'):
        minutos = int(sys.argv[idx +1 ])
    elif arg in ('-s'):
        segundo = int(sys.argv[idx +1 ])
    elif arg in ('-a'):
        alarma = int(sys.argv[idx +1 ])
tiempo = minutos * 60 + segundo

if tiempo < alarma:
    print("Error La alarma es mayor al timer ")
    if alarma == 20:
       print("La alarma por default es 20 ") 
    exit()
if alarma >= 60:
    print("Error La alarma debe se menor a 60  ")
    exit()
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()








black = (0,0,0)
white = (255,255,255)
red = (244, 67,54)
green = (0,255,0)

enelx = (69, 33, 128)

fuente = 500
fuente2 = 400
counter = tiempo + 1

text = str('GO :)')

timer_event = pygame.USEREVENT
pygame.time.set_timer(timer_event, 1000)

font = pygame.font.SysFont('Arial', fuente)

run = True
screen.fill(enelx)
while run:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1 

            if counter > 60:
                m, s = divmod(counter, 60)
                if m < 10:
                    m = '0'+ str(m)
                if s < 10:
                    s = '0'+ str(s)
                text = str(m)+':'+str(s)
            elif counter <= 60 and counter >= 10:
                text = str(counter).rjust(2) 
            elif counter <= 9 and counter >= 0:
                text = str(counter).rjust(2) 
            else:
                font = pygame.font.SysFont('Arial', fuente2)
                text =  'END :('

            if counter <= alarma:
                screen.fill(red)
            else: 
                screen.fill(enelx)

        if e.type == pygame.QUIT: 
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

    
    text2 = font.render(text, True, white )
    screen.blit( text2, text2.get_rect(center = screen.get_rect().center) ) 
    pygame.display.flip()


