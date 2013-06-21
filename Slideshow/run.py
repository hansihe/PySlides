__author__ = 'HansiHE'

import json
import time
import pygame
from serial_manager import SerialManager
from slideshow_manager import SlideshowManager

from slidetypes import image, movie, null
slide_types = {
    "image": image.ImageSlide,
    "movie": movie.MovieSlide,
    "null": null.NullSlide
}

screen_size = screen_width, screen_height = (1920, 1080)


def get_action_from_button(config, button_num):
    try:
        return config["button-mappings"][str(button_num)]
    except KeyError:
        print "action not found"
        return None

def process_input(slide_renderer, config, btn_num, btn_status):
    if btn_status == 0:
        action = get_action_from_button(config, btn_num)
        if action:
            slide_renderer.load_action(action)


pygame.init()

screen = pygame.display.set_mode(screen_size)

config = json.load(open("config.json", "r"))

slideRenderer = SlideshowManager(config, screen)
slideRenderer.load_default_slideshow()

serialManager = SerialManager(port="/dev/ttyAMA0", baudrate=9600)

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    serialManager.pool()
    btn_num, btn_status = serialManager.process()
    process_input(slideRenderer, config, btn_num, btn_status)

    slideRenderer.tick()

    time.sleep(0.1)

slideRenderer.destroy()
pygame.quit()
