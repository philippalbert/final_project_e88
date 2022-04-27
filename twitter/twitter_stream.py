import logging
import socket

from tweepy import StreamingClient



# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class StreamTwitter(StreamingClient):
    def __init__(self, c_socket):
        self.socket = c_socket

    def on_connect(self):
        super().on_connect()
        logger.debug("Connected to Twitter.")

    def on_data(self, raw_data):
        print(f"This is raw data:\n{raw_data}")
        self.socket.send(raw_data)
