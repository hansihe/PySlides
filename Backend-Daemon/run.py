__author__ = 'HansiHE'

from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineOnlyReceiver

class CommandReceiver(LineOnlyReceiver):
    """This is just about the simplest possible protocol"""

    def lineReceived(self, line):
        pass


def main():
    factory = protocol.ServerFactory()
    factory.protocol = CommandReceiver
    reactor.listenTCP(7455,factory)
    reactor.run()


if __name__ == '__main__':
    main()