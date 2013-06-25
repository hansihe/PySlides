__author__ = 'HansiHE'

from . import Slide
import subprocess
import pygame


class MovieSlide(Slide):

    def __init__(self, global_config, config, screen):
        super(MovieSlide, self).__init__(global_config, config, screen)

    def init(self):
        self.screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 36)
        text = font.render("Loading...", 1, (255, 255, 255))
        text_pos = text.get_rect()
        text_pos.centerx = self.screen.get_rect().centerx
        self.screen.blit(text, text_pos)

        self.flip_display()
        self.player = subprocess.Popen(['./omxplayer', self.global_config['media_dir'] + self.config['file']], stdin=subprocess.PIPE)
        print "rendering %s" % str(self.config)

    def tick(self, time):
        if self.player and self.player.poll():
            self.player = None
            return True

    def destroy(self):
        print "destroying player"
        if self.player:
            self.player.communicate(input='q')
            self.player.wait()