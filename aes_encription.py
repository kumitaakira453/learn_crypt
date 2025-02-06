import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class AESEncryption:
    def __init__(self):
        self.key = get_random_bytes(16)  # 128ビットのランダムな鍵

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode("utf-8"))
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode("utf-8")

    def decrypt(self, ciphertext):
        data = base64.b64decode(ciphertext)
        nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        decrypted_text = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_text.decode("utf-8")


# 使用例
aes_cipher = AESEncryption()
plaintext = "Hello, AES!"
ciphertext = aes_cipher.encrypt(plaintext)
print("Encrypted:", ciphertext)
decrypted_text = aes_cipher.decrypt(ciphertext)
print("Decrypted:", decrypted_text)
