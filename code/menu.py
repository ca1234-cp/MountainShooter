#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./esset/PRE_ORIG_SIZE.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):

        pygame.mixer_music.load('./esset/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

            #Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()  # close window
                   quit()  # end pygame
