__author__ = 'HansiHE'

import subprocess
import signal
from config import slideshow_path


class AlreadyRunningException(Exception):
    pass


class NotRunningException(Exception):
    pass


class RestartFailedException(Exception):
    pass


class SlideshowManager(object):

    slideshow_process = None

    def start_slideshow(self):
        if self.slideshow_process:
            raise AlreadyRunningException()
        self.slideshow_process = subprocess.Popen(['sudo', 'python', slideshow_path])

    def stop_slideshow(self):
        if not self.slideshow_process:
            raise NotRunningException()
        self.slideshow_process.send_signal(signal.SIGINT)

    def restart_slideshow(self):
        try:
            self.stop_slideshow()
        except NotRunningException:
            pass

        try:
            self.start_slideshow()
        except AlreadyRunningException:
            raise RestartFailedException()