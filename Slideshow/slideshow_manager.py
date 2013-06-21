__author__ = 'HansiHE'

from slideshow_renderer import SlideshowRenderer


class SlideshowManager(object):

    config = None
    screen = None

    slideshow = None

    slideshow_name = None

    def __init__(self, config, screen):
        self.config = config
        self.screen = screen

    def load_default_slideshow(self):
        self.load_action(self.config['default_action'])

    def get_slideshow_config_by_name(self, name):
        return self.config['slideshows'][name]

    def load_slideshow(self, slideshow_name):
        print "loading slideshow %s" % slideshow_name
        if self.slideshow:
            self.slideshow.destroy()
        self.slideshow_name = slideshow_name
        self.slideshow = SlideshowRenderer(self.config, self.slideshow_name, self.screen)

    def get_slideshow_name_by_action(self, action_name):
        return self.config['actions'][action_name]

    def load_action(self, action_name):
        try:
            self.load_slideshow(self.get_slideshow_name_by_action(action_name))
        except KeyError:
            print "action not found"

    def tick(self):
        if self.slideshow and self.slideshow.tick():
            self.load_action("default")

    def destroy(self):
        if self.slideshow:
            self.slideshow.destroy()