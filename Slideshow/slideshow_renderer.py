__author__ = 'HansiHE'

import datetime
from slidetypes import slide_types


class SlideshowRenderer(object):  # Handles rendering a slideshow

    config = None
    slideshow_name = None
    screen = None

    current_slide = 0
    num_slides = None

    slide = None
    last = None

    def __init__(self, config, slideshow_name, screen):
        self.config = config
        self.slideshow_name = slideshow_name
        self.screen = screen
        self.num_slides = len(self.config['slideshows'][self.slideshow_name]['slides'])
        self.load_slide_num(self.current_slide)

    def get_slide_name(self, slide_number):
        print self.config['slideshows'][self.slideshow_name]['slides'][slide_number]
        return self.config['slideshows'][self.slideshow_name]['slides'][slide_number]

    def get_slide_config(self, slide_name):
        return self.config['slides'][slide_name]

    def update_time(self):
        self.last = datetime.datetime.utcnow()

    def next_slide(self):
        self.current_slide += 1
        self.load_slide_num(self.current_slide)

    def load_slide_num(self, slide_num):
        self.load_slide_name(self.get_slide_name(slide_num))

    def destroy_current_slide(self):
        if self.slide:
            self.slide.destroy()

    def load_slide_name(self, slide_name):
        import cProfile
        self.destroy_current_slide()
        slide_conf = self.get_slide_config(slide_name)
        self.slide = slide_types[slide_conf['type']](self.config, slide_conf, self.screen)
        #cProfile.runctx("self.slide.init()", globals(), locals(), sort="time")
        self.slide.init()
        self.update_time()

    def tick(self):
        if self.slide and self.slide.tick((datetime.datetime.utcnow() - self.last).total_seconds()):
            if (self.current_slide+1) >= self.num_slides:
                self.destroy_current_slide()
                return True
            self.next_slide()

    def destroy(self):
        self.destroy_current_slide()