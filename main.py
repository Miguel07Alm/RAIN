import pygame as pg
from pygame import *
import random
from pygame.locals import *
import os
import time

pg.init()
pg.mixer.init()

DIR = os.path.dirname(os.path.realpath(__file__))


WIN = pg.display.set_mode((600,800))
pg.display.set_caption("CHILL RAIN")

water_img = pg.transform.scale(pg.image.load(os.path.join(DIR, "water.png")).convert_alpha(), (30,30))
bg_img = pg.transform.scale(pg.image.load(os.path.join(DIR, "bg.png")).convert(), (600,800))

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
        self.rect.x = random.randint(50,550)
        self.rect.y = self.rect.y + displacement
        
    def draw(self, win):     
        win.blit(self.img, (self.rect.x, self.rect.y))
def show_window(win, raining):
    win.blit(bg_img, (0,0))
    for rain in raining:
        rain.draw(win)
            
    pg.display.flip()

def main():
    global WIN
    clock = pg.time.Clock()
    raining = [Water(random.randint(50,550), random.randint(0,750))]
    pg.mixer.Channel(0).play(pg.mixer.Sound(os.path.join(DIR, "lluvia.wav")),-1)
    add_rain = False
    run = True
    while run:
        clock.tick(60)
        events = pg.event.get()
        rem_rain = []
        for event in events:
            if event.type == pg.QUIT:
                run = False
                
        for rain in raining:  
            if rain.rect.y > 600:
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