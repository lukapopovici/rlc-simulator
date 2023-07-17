import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import subprocess
import numpy as np
import matplotlib.pyplot as plot
import math 
bg = pygame.image.load("assets/background.png")
pygame.init()
pygame.display.set_caption('Circuit RLC                         Luka Popovici CTI                           github: lukapopovici')
def render_graph(R,L,C,V,Hz):
    b=R/(2*L)
    omega=1/math.sqrt((L*C))
    e=2.71
    time        = np.arange(0, 300, 1);
    amplitude   = V*(e**(-b*time))*np.sin(np.sqrt(omega**2-b**2)*time + Hz)
    plot.plot(time, amplitude)
    plot.title('Functia tensiunii pe bornele capacitorului')
    plot.xlabel('Timpul (t) in nanosecunde')
    plot.ylabel('Tensiune (V)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show()
    plot.show()
def get_string():
    with open('fisiere/enunt.txt', 'r') as file:
     data = file.read()
    return str(data)
string=get_string()
# GLOBAL VARIABLES
alb = (255, 255, 255)
WIDTH = 600
HEIGHT = 600
FONT = pygame.font.SysFont('Arial', 20)
FONT_COLOR = pygame.Color('black')
class buton(pygame.sprite.Sprite):

    def __init__(self, pos, element):
        pygame.sprite.Sprite.__init__(self)
        ATOM_IMG = pygame.image.load(r'assets/red.jpg')
        ATOM_IMG = pygame.transform.scale(ATOM_IMG,(100,70))
        self.image = ATOM_IMG.copy()
        textsurface = FONT.render(element, True, FONT_COLOR)
        textrect = textsurface.get_rect(center=self.image.get_rect().center)
        self.image.blit(textsurface, textrect)
        self.rect = self.image.get_rect(center=pos)
class TEXT(pygame.sprite.Sprite):

    def __init__(self, pos, element):
        pygame.sprite.Sprite.__init__(self)
        ATOM_IMG = pygame.image.load(r'assets/bland.jpg')
        ATOM_IMG = pygame.transform.scale(ATOM_IMG,(600,50))
        self.image = ATOM_IMG.copy()
        textsurface = FONT.render(element, True, FONT_COLOR)
        textrect = textsurface.get_rect(center=self.image.get_rect().center)
        self.image.blit(textsurface, textrect)
        self.rect = self.image.get_rect(center=pos)
class BOB(pygame.sprite.Sprite):

    def __init__(self, pos, element):
        pygame.sprite.Sprite.__init__(self)
        ATOM_IMG = pygame.image.load(r'assets/bob.jpg')
        ATOM_IMG = pygame.transform.scale(ATOM_IMG,(100,50))
        self.image = ATOM_IMG.copy()
        textsurface = FONT.render(element, True, FONT_COLOR)
        textrect = textsurface.get_rect(center=self.image.get_rect().center)
        self.image.blit(textsurface, textrect)
        self.rect = self.image.get_rect(center=pos)
class REZ(pygame.sprite.Sprite):

    def __init__(self, pos, element):
        pygame.sprite.Sprite.__init__(self)
        ATOM_IMG = pygame.image.load(r'assets/rez.jpg')
        ATOM_IMG = pygame.transform.scale(ATOM_IMG,(62,62))
        self.image = ATOM_IMG.copy()
        textsurface = FONT.render(element, True, FONT_COLOR)
        textrect = textsurface.get_rect(center=self.image.get_rect().center)
        self.image.blit(textsurface, textrect)
        self.rect = self.image.get_rect(center=pos)
class VOL(pygame.sprite.Sprite):

    def __init__(self, pos, element):
        pygame.sprite.Sprite.__init__(self)
        ATOM_IMG = pygame.image.load(r'assets/vol2.png')
        ATOM_IMG = pygame.transform.scale(ATOM_IMG,(60,60))
        self.image = ATOM_IMG.copy()
        textsurface = FONT.render(element, True, FONT_COLOR)
        textrect = textsurface.get_rect(center=self.image.get_rect().center)
        self.image.blit(textsurface, textrect)
        self.rect = self.image.get_rect(center=pos)
class CAP(pygame.sprite.Sprite):

    def __init__(self, pos, element):
        pygame.sprite.Sprite.__init__(self)
        ATOM_IMG = pygame.image.load(r'assets/cap.jpg')
        ATOM_IMG = pygame.transform.scale(ATOM_IMG,(60,60))
        self.image = ATOM_IMG.copy()
        textsurface = FONT.render(element, True, FONT_COLOR)
        textrect = textsurface.get_rect(center=self.image.get_rect().center)
        self.image.blit(textsurface, textrect)
        self.rect = self.image.get_rect(center=pos)
def get_values():
   with open('fisiere/test.txt') as f:
    content = f.readlines()
    li = [x.strip() for x in content]
    re=li[0]
    imp=li[1]
    cap=li[2]
    vol=li[3]
    her=li[4]
   return re,imp,cap,vol,her

pygame_icon = pygame.image.load('assets/coil.png')
pygame.display.set_icon(pygame_icon)

pygame.init()

negru = (0, 0, 0)  
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
  
all_sprites_list = pygame.sprite.Group()

buton_calcule=buton((100,100),'Calcule')
buton_calcule.rect.x=500
buton_calcule.rect.y=550

buton_graf=buton((100,100),' Graf uc(t) ')
buton_graf.rect.x=300
buton_graf.rect.y=550

buton_meniu=buton((100,100),'Valori RLC')
buton_meniu.rect.x=0
buton_meniu.rect.y=550

rezistor = REZ((150, 200), ' ')
rezistor.rect.x = 200
rezistor.rect.y = 300

bobina = BOB((150, 200), ' ')
bobina.rect.x = 300
bobina.rect.y = 305

capacitor = CAP((150, 200), ' ')
capacitor.rect.x = 400
capacitor.rect.y = 300

sursa = VOL((150, 200), ' ')
sursa.rect.x = 100
sursa.rect.y = 300

text=TEXT((500,200),string)
text.rect.x=100
text.rect.y=50

all_sprites_list.add(buton_graf)
all_sprites_list.add(rezistor)
all_sprites_list.add(bobina)
all_sprites_list.add(capacitor)
all_sprites_list.add(sursa)
all_sprites_list.add(buton_calcule)
all_sprites_list.add(buton_meniu)

exit = True
R,I,C,S,H=get_values()
def update_txt(valoare):
    text=TEXT((10,10),valoare)
    text.rect.x=0
    text.rect.y=0
    all_sprites_list.draw(screen)
    all_sprites_list.add(text)
    pygame.display.flip()
string=get_string()
update_txt("")
while exit:
    R,I,C,S,H=get_values()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = event.pos
            if rezistor.rect.collidepoint(x,y):
                update_txt(str("Valoarea rezistorului este "+R+" Ω"))
            if bobina.rect.collidepoint(x,y):
                update_txt(str("Valoarea bobinei este "+I+" H"))
            if capacitor.rect.collidepoint(x,y):
                update_txt(str("Valoarea capacitor este "+C+" F"))
            if sursa.rect.collidepoint(x,y):
                update_txt(str("Conditiile initiale sunt Uc(0) "+S+" V si φ "+H))
            if buton_meniu.rect.collidepoint(x,y):
                subprocess.Popen("exe/meniu.exe")
                R,I,C,S,H=get_values()
                continue
            if buton_calcule.rect.collidepoint(x,y):
                process=subprocess.Popen("exe/enunturi.exe")
                process.wait()
                string=get_string()
                update_txt(string)
                continue
            if buton_graf.rect.collidepoint(x,y):
                 B=float(float(R)/(float(I)*2))
                 OMEGA=float(1/(math.sqrt(float(I)*float(C))))
                 if B < OMEGA:
                    render_graph(float(R),float(I),float(C),float(S),float(H))
                 else:
                     update_txt(str("Nu oscileaza!"))
                 continue
                
                
                        
    screen.blit(bg,(0,20))
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.draw.line(screen, negru, (160, 330), (500, 330))
    pygame.draw.line(screen, negru, (500, 330), (500, 500))
    pygame.draw.line(screen, negru, (500, 500), (130, 500))
    pygame.draw.line(screen, negru, (130, 500), (130, 360))
    pygame.display.flip()
  
pygame.quit()
