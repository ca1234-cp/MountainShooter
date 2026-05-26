#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self, ):
        pygame.mixer_music.load('./esset/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
        # for event in pygame.event.get():
            #if event.type == pygame.QUIT:
               # pygame.quit()  # close window
               # quit()  # end pygame
