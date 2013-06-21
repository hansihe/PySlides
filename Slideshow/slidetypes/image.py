__author__ = 'HansiHE'

from . import Slide
import pygame


class ImageSlide(Slide):

    def __init__(self, config, screen):
        super(ImageSlide, self).__init__(config, screen)

    def init(self):
        self.screen.fill((255,255,255))

        image_slide = pygame.image.load(self.config['file']).convert()
        self.screen.blit(image_slide, (0, 0))
        self.flip_display()

        print "rendering %s" % str(self.config)

    def tick(self, time):
        return self.config.has_key('time') and time >= self.config['time']
