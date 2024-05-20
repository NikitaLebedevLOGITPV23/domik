import pygame
import sys
import random
pygame.init()

#1

#värvid
#lGreen = [153, 255, 153]
#lBlue = [153, 204, 255]

#ekraani_pind=pygame.display.set_mode( (640, 480))
#ekraani_pind.fill(lGreen)
#pygame.display.set_caption("Esimene Mäng")

#gameover=False 

#while not gameover:
#    youWin=pygame.image.load("chad.jpg")
#    youWin=pygame.transform.scale(youWin, [300,200])
#    ekraani_pind.blit(youWin,[180,100])
    
#    pygame.display.flip()
#    for i in pygame.event.get():
#        if i.type==pygame.QUIT:
#            sys.exit()
#pygame.quit

   
#2

#r=random.randint(0,255)
#g=random.randint(0,255)
#b=random.randint(0,255)
#varv=[r,g,b]
#lGrey=[169,169,169]

#pind=pygame.display.set_mode([640,480])
#pygame.display.set_caption("Juhuslikud kujundid")
#pind.fill(lGrey)

#for i in range(1,10):
#    x=random.randint(0,635)
#    y=random.randint(0,475)
#    pygame.draw.rect(pind, varv, [x,y,15,15])

#    pygame.display.flip()
#while True:
#    event=pygame.event.poll()
#    if event.type==pygame.event.poll():
#        break
#pygame.quit()

#3
import pygame
import random

def Maja(x, y, laius, kõrgus, pind, varv):
    punktid = [(x, y - ((3 / 4.0) * kõrgus)),(x, y),(x + laius, y),(x + laius, y - (3 / 4.0) * kõrgus),(x, y - ((3 / 4.0) * kõrgus)),(x + laius / 2.0, y - kõrgus),(x + laius, y - (3 / 4.0) * kõrgus)]
    suurus = random.randint(1, 10)
    pygame.draw.lines(pind, varv, False, punktid, suurus)

def Uks(x, y, laius, kõrgus, pind, varv):
    punktid = [(x, y),(x, y - (1 / 2) * kõrgus),(x + (1 / 3) * laius, y - (1 / 2) * kõrgus),(x + (1 / 3) * laius, y),(x, y)]
    suurus = random.randint(1, 10)
    pygame.draw.lines(pind, varv, True, punktid, suurus)

def Aken(x, y, laius, kõrgus, pind, varv):
    punktid = [(x, y),(x, y - (1 / 3) * kõrgus),(x + (1 / 3) * laius, y - (1 / 3) * kõrgus),(x + (1 / 3) * laius, y),(x, y)]
    suurus = random.randint(1, 10)
    pygame.draw.lines(pind, varv, True, punktid, suurus)

#def drawHouse(x, y, laius, kõrgus, pind, varv):
#    points = [(x,y- ((3/4.0) * kõrgus)), (x,y), (x+laius,y), (x+laius,y-(3/4.0) * kõrgus), (x,y- ((3/4.0) * kõrgus)), (x + laius/2.0,y-kõrgus), (x+laius,y-(3/4.0)*kõrgus)]
#    lineThickness = 8
#    pygame.draw.lines(pind, varv, False, points, lineThickness)

pygame.init()
lGrey = [169, 169, 169]
red = [255, 0, 0]

pind = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Maja")
pind.fill(lGrey)

Maja(100, 400, 500, 400, pind, red)
Uks(200, 300, 300, 300, pind, red)
Aken(400, 500, 600, 500, pind, red)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

