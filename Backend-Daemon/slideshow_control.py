__author__ = 'HansiHE'

from twisted.web import resource
from slideshow_manager import SlideshowManager


slideshow_manager = SlideshowManager()

class SlideshowControl(resource.Resource):
    isLeaf = False

slideshow_control = SlideshowControl()

class SlideshowRestart(resource.Resource):
    isLeaf = True

    def render_POST(self, request):
        return 'ye'

slideshow_restart = SlideshowRestart()

slideshow_control.putChild('restart', slideshow_restart)