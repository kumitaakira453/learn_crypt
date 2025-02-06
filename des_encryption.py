import base64

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


class DESEncryption:
    def __init__(self):
        self.key = get_random_bytes(8)  # DESは8バイトの鍵を使用

    def encrypt(self, plaintext):
        cipher = DES.new(self.key, DES.MODE_ECB)
        padded_text = self.pad(plaintext)
        ciphertext = cipher.encrypt(padded_text.encode("utf-8"))
        return base64.b64encode(ciphertext).decode("utf-8")

    def decrypt(self, ciphertext):
        cipher = DES.new(self.key, DES.MODE_ECB)
        ciphertext = base64.b64decode(ciphertext)
        decrypted_text = cipher.decrypt(ciphertext).decode("utf-8")
        return self.unpad(decrypted_text)

    def pad(self, text):
        """DESは8の倍数のブロックサイズを要求するためパディングを追加している"""
        while len(text) % 8 != 0:
            text += " "
        return text

    def unpad(self, text):
        """パディングを取り除く"""
        return text.rstrip()


des_cipher = DESEncryption()
plaintext = "Hello, DES!"
ciphertext = des_cipher.encrypt(plaintext)
print("Encrypted:", ciphertext)
decrypted_text = des_cipher.decrypt(ciphertext)
print("Decrypted:", decrypted_text)
