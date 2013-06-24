__author__ = 'HansiHE'

from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineOnlyReceiver

from command import commands


class CommandReceiver(LineOnlyReceiver):
    """This is just about the simplest possible protocol"""

    delimiter = '\n'

    def lineReceived(self, line):
        try:
            split_index = line.index(' ')
            command_name = line[:split_index]
            command_data = line[split_index+1:]
        except ValueError:
            command_name = line
            command_data = ""

        try:
            commands[command_name](command_data)
        except KeyError:
            return


def main():
    print 'wat'
    factory = protocol.ServerFactory()
    factory.protocol = CommandReceiver
    reactor.listenTCP(7455, factory, interface='localhost')
    reactor.run()


if __name__ == '__main__':
    main()