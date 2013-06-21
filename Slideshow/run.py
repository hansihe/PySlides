__author__ = 'HansiHE'

import json
import datetime
import time
import serial
import pygame
import sys

from slidetypes import image, movie, null
slide_types = {
    "image": image.ImageSlide,
    "movie": movie.MovieSlide,
    "null": null.NullSlide
}

screen_size = screen_width, screen_height = (1920, 1080)


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
        self.destroy_current_slide()
        slide_conf = self.get_slide_config(slide_name)
        self.slide = slide_types[slide_conf['type']](slide_conf, self.screen)
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

def get_action_from_button(config, button_num):
    try:
        return config["button-mappings"][str(button_num)]
    except KeyError:
        print "action not found"
        return None

def process_message(msg, slide_renderer, config):
    print msg
    button_data = msg.split(":")
    print button_data

    if button_data[1] == "0":  # 0 is a button press due to internal pull-ups
        action = get_action_from_button(config, button_data[0])
        if action:
            slide_renderer.load_action(action)


pygame.init()

screen = pygame.display.set_mode(screen_size)

config = json.load(open("config.json", "r"))

slideRenderer = SlideshowManager(config, screen)
slideRenderer.load_default_slideshow()

port = serial.Serial(port="/dev/ttyAMA0", baudrate=9600)

recv_buffer = ""

newline_str = "\r\n"

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    recv_buffer += port.read(port.inWaiting())
    while newline_str in recv_buffer:
        num_char = recv_buffer.index(newline_str)
        process_message(recv_buffer[:num_char], slideRenderer, config)
        recv_buffer = recv_buffer[num_char+len(newline_str):]
    slideRenderer.tick()

    time.sleep(0.1)

slideRenderer.destroy()
pygame.quit()
