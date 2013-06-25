__author__ = 'HansiHE'

from twisted.web import server, resource
from twisted.internet import reactor


class RootResource(resource.Resource):
    isLeaf = False

root = RootResource()

from slideshow_control import slideshow_control
root.putChild('slideshow', slideshow_control)

reactor.listenTCP(8080, server.Site(root))
reactor.run()