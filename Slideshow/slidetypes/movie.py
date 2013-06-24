__author__ = 'HansiHE'

from . import Slide
import subprocess
import time


class MovieSlide(Slide):

    def __init__(self, global_config, config, screen):
        super(MovieSlide, self).__init__(global_config, config, screen)

    def init(self):
        self.screen.fill((0, 0, 255))
        self.flip_display()
        self.player = subprocess.Popen(['omxplayer', self.global_config['media_dir'] + self.config['file']], stdin=subprocess.PIPE)
        print "rendering %s" % str(self.config)

    def tick(self, time):
        if self.player and self.player.poll():
            self.player = None
            return True

    def destroy(self):
        print "destroying player"
        if self.player:
            #self.player.communicate(input="q")
            self.player.communicate(input='q')
            #self.player.terminate()
            self.player.wait()
            #self.player = None
            #time.sleep(5)
            #init_display()
            #subprocess.call("sudo fbset -depth 8 && sudo fbset -depth 16", shell=True)
            time.sleep(5)