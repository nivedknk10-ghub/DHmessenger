import random
class DiffieHellman:
    def __init__(self,g,p):
        self.p = p
        self.g = g
        self.private_key = random.randint(2, p-2)
        self.public_key = pow(g, self.private_key, self.p)

    def generate_shared_key(self, other_public_key):
        shared_key = pow(other_public_key, self.private_key, self.p)
        return shared_key
