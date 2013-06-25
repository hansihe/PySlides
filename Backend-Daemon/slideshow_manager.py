__author__ = 'HansiHE'

import subprocess
from config import slideshow_path


class SlideshowManager(object):

    slideshow_process = None

    def __init__(self):
        self.slideshow_process = subprocess.Popen(['sudo', 'python', slideshow_path])