import socket
import pickle
from dh import DiffieHellman
from secure_channel import SecureChannel

class Client:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.dh = DiffieHellman(5,23)

    def start(self):
        s = socket.socket()
        s.connect((self.host, self.port))

        server_pub = pickle.loads(s.recv(1024))
        shared_key = self.dh.generate_shared_key(server_pub)

        s.send(pickle.dumps(self.dh.public_key))

        channel = SecureChannel(shared_key)

        while True:
            msg = input("you: ")
            s.send(channel.encrypt(msg))

            data = s.recv(1024)
            print(f'server:{channel.decrypt(data)}')
