import socket
from argparse import ArgumentParser

from tweepy import Client, StreamRule

from twitter.twitter_stream import StreamTwitter

print("Start program")

# define host and port for socket
HOST = "0.0.0.0"
PORT = 5555

parser = ArgumentParser()
# for example purposes
parser.add_argument("--use_history", default=True, type=bool)
# for authentication
parser.add_argument("--bearer", default="", type=str, help="Add bearer authentication for twitter api")
# get parser arguments
p_a = parser.parse_args()


def run_twitter_stream(c_socket=None):
    # twitter id of o2 germany account
    o2_id = 76713761

    if p_a.use_history:
        print('Fake stream running')
        twitter_client = Client(p_a.bearer)
        res = twitter_client.get_users_mentions(id=o2_id)
        print(res)
    else:
        print('Real stream running')
        # create a streaming client
        s_t = StreamTwitter(p_a.bearer, c_socket)
        # add rule to stream
        s_t.add_rules(StreamRule(id=o2_id))
        # start stream with defined filter
        s_t.filter()


if __name__ == '__main__':
    print(f'Start creating socket')
    # create socket
    s_socket = socket.socket()
    s_socket.bind((HOST, PORT))
    # make server accept connections
    # 4 specifies number of unaccepted connections that the system will allow before refusing new connections.
    s_socket.listen()
    print(f'Created server site socket with host {HOST} and port {PORT}')

    # get client socket to propagate to twitter api
    c_socket, _ = s_socket.accept()

    run_twitter_stream(c_socket)
    s_socket.close()
