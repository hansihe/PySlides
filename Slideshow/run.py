__author__ = 'HansiHE'

import json
import time
import pygame
import lockfile
from serial_manager import SerialManager
from slideshow_manager import SlideshowManager

screen_size = screen_width, screen_height = (1920, 1080)


def get_action_from_button(config, button_num):
    try:
        return config["button-mappings"][str(button_num)]
    except KeyError:
        print "action not found"
        return None

def process_input(slide_renderer, config, btn_data):
    btn_num, btn_status = btn_data
    if btn_status == "0":
        action = get_action_from_button(config, btn_num)
        if action:
            slide_renderer.load_action(action)


pygame.init()

screen = pygame.display.set_mode(screen_size)

lock = lockfile.FileLock('../config/config.json')
with lock:
    config = json.load(open(lock.path))
#config = json.load(open("../config/config.json", "r"))

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
    data = serialManager.process()
    if data:
        process_input(slideRenderer, config, data)

    slideRenderer.tick()

    time.sleep(0.05)


serialManager.close()
slideRenderer.destroy()
pygame.quit()
