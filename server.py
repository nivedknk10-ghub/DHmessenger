import socket
import pickle
from dh import DiffieHellman
from secure_channel import SecureChannel

class Server:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.dh = DiffieHellman(5,23)

    def start(self):
        #create socket, bind it with port and start listening
        s = socket.socket()
        s.bind((self.host, self.port))
        s.listen(1)

        print("Waiting for a connection...")
        #accept socket object and client address
        conn, addr = s.accept()
        print(f'Connected by: {addr}')

        #send public key to client, for it calculate the shared key
        conn.send(pickle.dumps(self.dh.public_key))

        #accept the public key send by the client
        client_pub = pickle.loads(conn.recv(1024))

        #calculate shared key
        shared_key = self.dh.generate_shared_key(client_pub)
        print("Shared key established...")

        #create channel object with the calculated shared_key
        channel = SecureChannel(shared_key)

        while True:
            #recieve data
            data = conn.recv(1024)
            #create exit condition
            if not data:
                break

            #decrypt the received data and print it
            message = channel.decrypt(data)
            print(f"client: {message}")

            #accept reply from input, encrypt it and send it over the socket object
            reply = input("You: ")
            conn.send(channel.encrypt(reply))

        conn.close()
