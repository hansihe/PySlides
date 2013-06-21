__author__ = 'HansiHE'

import serial
import re


class SerialManager(object):

    newline_separator = None
    data_format = None
    buffer = ""
    port = None

    def __init__(self, newline_separator="\r\n", data_format=re.compile(r'(\d+):(\d+)'), **kwargs):
        """
        Takes newline_separator, passes the other arguments to serial.Serial
        """

        self.newline_separator = newline_separator
        self.data_format = data_format
        self.port = serial.Serial(**kwargs)

    def pool(self):
        """
        Pools data from the serial port and adds it to the internal buffer.
        """

        buffer += self.port.read(self.port.inWaiting())

    def has_data(self):
        """
        Returns True if the buffer has readable data in it.
        """

        return self.newline_separator in self.buffer

    def read(self):
        """
        Reads one line from the buffer and returns it.
        """

        num_char = self.buffer.index(self.newline_separator)
        result = self.buffer[num_char]
        self.buffer = self.buffer[num_char+len(self.newline_separator):]
        return result

    def process(self):
        """
        Goes through all data in buffer and returns only the ONE most recent press.
        """

        if self.has_data():
            last_data = None
            while self.has_data():
                last_data = self.read()

            match = self.data_format.match(last_data)

            if not match:
                raise ValueError("Invalid buffer data was supplied.")

            return match.groups()