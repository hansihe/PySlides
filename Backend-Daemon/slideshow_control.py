__author__ = 'HansiHE'

from twisted.web import resource
from slideshow_manager import SlideshowManager, RestartFailedException, NotRunningException, AlreadyRunningException
import json


slideshow_manager = SlideshowManager()


class SlideshowControl(resource.Resource):
    isLeaf = False

slideshow_control = SlideshowControl()


class SlideshowStart(resource.Resource):
    isLeaf = True

    def render_POST(self, request):
        try:
            slideshow_manager.start_slideshow()
        except Exception, e:
            return json.dumps({'success': False, 'exception': str(e)})
        return json.dumps({'success': True})

slideshow_start = SlideshowStart()


class SlideshowStop(resource.Resource):
    isLeaf = True

    def render_POST(self, request):
        try:
            slideshow_manager.stop_slideshow()
        except Exception, e:
            return json.dumps({'success': False, 'exception': str(e)})
        return json.dumps({'success': True})

slideshow_stop = SlideshowStop()


class SlideshowRestart(resource.Resource):
    isLeaf = True

    def render_POST(self, request):
        try:
            slideshow_manager.restart_slideshow()
        except Exception, e:
            return json.dumps({'success': False, 'exception': str(e)})
        return json.dumps({'success': True})

slideshow_restart = SlideshowRestart()

slideshow_control.putChild('start', slideshow_start)
slideshow_control.putChild('stop', slideshow_stop)
slideshow_control.putChild('restart', slideshow_restart)