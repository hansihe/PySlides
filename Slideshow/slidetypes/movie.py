__author__ = 'HansiHE'

from . import Slide
import subprocess


class MovieSlide(Slide):

    def __init__(self, config, screen):
        super(MovieSlide, self).__init__(config, screen)

    def init(self):
        self.screen.fill((0, 0, 255))
        self.flip_display()
        self.player = subprocess.Popen(['omxplayer', self.config['file']], stdin=subprocess.PIPE)
        print "rendering %s" % str(self.config)

    def tick(self, time):
        if self.player and self.player.poll():
            self.player = None
            return True

    def destroy(self):
        print "destroying player"
        if self.player:
            self.player.communicate(input="q")
            self.player.wait()
            self.player = None