__author__ = 'HansiHE'

from . import Slide

class NullSlide(Slide):
    def __init__(self, config, screen):
        super(NullSlide, self).__init__(config, screen)

    def init(self):
        self.screen.fill((255,255,255))
        self.flip_display()

        print "rendering %s" % str(self.config)

    def tick(self, time):
        return time > self.config['time']
