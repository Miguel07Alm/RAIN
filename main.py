import pygame as pg
from pygame.gfxdraw import *
from pygame import *
import random
from pygame.locals import *
import os
import time

pg.init()
pg.mixer.init()

DIR = os.path.dirname(os.path.realpath(__file__))
IMGS_DIR = os.path.join(DIR, "imgs")
MUSIC_DIR = os.path.join(DIR, "audio")

time = pg.time.get_ticks()
twinkle_yell = [(255,255,0), (255,255,100), (255,255,153)]
twinkle_red= [(255,0,0), (220,20,60), (128,0,0)]

WIN = pg.display.set_mode((600,800))
pg.display.set_caption("RELAXING RAIN")

water_img = pg.transform.scale(pg.image.load(os.path.join(IMGS_DIR, "water.png")).convert_alpha(), (5,5))
bg_img = pg.transform.scale(pg.image.load(os.path.join(IMGS_DIR, "bg.png")).convert(), (600,800))

class Water:
    img = water_img
    vel = 25
    def __init__(self,x,y):
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.tick_count = 0
        self.rect.y = y
        self.passed = False
    def move(self):
        self.tick_count += 1
        
        displacement = self.vel * self.tick_count + 0.5 * (3) * (self.tick_count) **2
        if displacement >= 16:
            displacement = (displacement/abs(displacement)) * 16
        if displacement < 0:
            displacement -= 2
        self.rect.x = random.randint(0,550)
        self.rect.y = self.rect.y + displacement
        
    def draw(self, win):     
        win.blit(self.img, (self.rect.x, self.rect.y))
def show_window(win, raining):
    win.blit(bg_img, (0,0))
    pg.gfxdraw.filled_circle(win, 50,100, 1,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 80,200, 1,random.choice(twinkle_red))
    pg.gfxdraw.filled_circle(win, 200,50, 2,random.choice(twinkle_red))
    pg.gfxdraw.filled_circle(win, 20,10, 2,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 30,80, 2,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 40,125, 2,random.choice(twinkle_red))
    pg.gfxdraw.filled_circle(win, 300,150, 3,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 40,180, 2,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 11,102, 3,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 156,128, 1,random.choice(twinkle_red))
    pg.gfxdraw.filled_circle(win, 67,114, 1,random.choice(twinkle_red))
    pg.gfxdraw.filled_circle(win, 89,72, 2,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 47,89, 2,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 45,220, 1,random.choice(twinkle_red))
    pg.gfxdraw.filled_circle(win, 400,143, 2,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 321,67, 2,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 350,120, 1,random.choice(twinkle_red))
    pg.gfxdraw.filled_circle(win, 21,234, 2,random.choice(twinkle_yell))
    pg.gfxdraw.filled_circle(win, 80,212, 2,random.choice(twinkle_yell))
    for rain in raining:
        rain.draw(win)
            
    pg.display.flip()

def main():
    global WIN
    clock = pg.time.Clock()
    raining = [Water(random.randint(0,550), random.randint(0,750))]
    pg.mixer.Channel(0).play(pg.mixer.Sound(os.path.join(MUSIC_DIR, "lluvia.wav")),-1)
    add_rain = False
    run = True
    while run:
        clock.tick(30)
        events = pg.event.get()
        rem_rain = []
        for event in events:
            if event.type == pg.QUIT:
                run = False
                
        for rain in raining:  
            if rain.rect.x > 600:
                rem_rain.append(rain)
            if not rain.passed and rain.rect.y > 800:
                rain.passed = True
                add_rain = True
        if add_rain:
            raining.append(Water(random.randint(0,550), random.randint(0,750)))
            
                    
        for r in rem_rain:
            raining.remove(r)
        for rain in raining:
            rain.move() 
                
                
                
        show_window(WIN, raining)
        
    
if __name__ == '__main__':
    main()