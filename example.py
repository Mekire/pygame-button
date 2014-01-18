import os
import sys
import random
import pygame as pg

from button import Button


os.environ["SDL_VIDEO_CENTERED"] = '1'
pg.init()


RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,180,0)


#The button can be styled in a manner similar to CSS.
BUTTON_STYLE = {"hover_color" : BLUE,
                "clicked_color" : GREEN,
                "clicked_font_color" : BLACK,
                "hover_font_color" : ORANGE,
                "hover_sound" : pg.mixer.Sound("blipshort1.wav")}


class Control(object):
    def __init__(self):
        self.screen = pg.display.set_mode((500,500))
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.done = False
        self.fps = 60.0
        self.color = WHITE
        message = "Change the screen color."
        self.button = Button((0,0,200,50),RED, self.change_color,
                             text=message, **BUTTON_STYLE)
        self.button.rect.center = (self.screen_rect.centerx,100)

    def change_color(self):
        self.color = [random.randint(0,255) for _ in range(3)]

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.button.check_event(event)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.screen.fill(self.color)
            self.button.update(self.screen)
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    run_it = Control()
    run_it.main_loop()
    pg.quit()
    sys.exit()