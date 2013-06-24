__author__ = 'HansiHE'

from . import Slide
import pygame


class ImageSlide(Slide):

    def __init__(self, global_config, config, screen):
        super(ImageSlide, self).__init__(global_config, config, screen)

    def init(self):
        self.screen.fill((255,255,255))

        if self.config['_cached_image']:
            image_slide = self.config['_cached_image']
            print 'loading image from memory cache'
        else:
            image_slide = pygame.image.load(self.global_config['media_dir'] + self.config['file'])#.convert()
        self.screen.blit(image_slide, (0, 0))
        self.flip_display()

        print "rendering %s" % str(self.config)

    def tick(self, time):
        return self.config.has_key('time') and time >= self.config['time']

    @classmethod
    def load_cache(cls, global_config, config):
        config['_cached_image'] = pygame.image.load(global_config['media_dir'] + config['file']).convert()