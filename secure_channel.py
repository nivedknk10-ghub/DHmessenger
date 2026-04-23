import hashlib
import dh

class SecureChannel:
    def __init__(self,shared_key):
        self.key = hashlib.sha256(str(shared_key).encode()).digest()

    def encrypt(self, message):
        message_bytes = message.encode()
        encrypted = bytes([b ^ self.key[i % len(self.key)] for i,b in enumerate(message_bytes)])
        return encrypted

    def decrypt(self, ciphertext):
        decrypted = bytes([b ^ self.key[i % len(self.key)] for i,b in enumerate(ciphertext)])
        return decrypted.decode()
