__author__ = 'HansiHE'

import pygame


class Slide(object):

    def __init__(self, global_config, config, screen):
        self.global_config = global_config
        self.config = config
        self.screen = screen

    def init(self):
        pass

    def tick(self, time):
        return True

    def destroy(self):
        pass

    def flip_display(self):
        pygame.display.flip()


import image, movie, null
slide_types = {
    "image": image.ImageSlide,
    "movie": movie.MovieSlide,
    "null": null.NullSlide
}