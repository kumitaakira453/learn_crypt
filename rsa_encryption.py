import rsa


class RSAEncryption:
    def __init__(self):
        # 公開鍵と秘密鍵のペアを生成(512bitで作成しているが実際には2048bit以上の方がいいらしい)
        (self.public_key, self.private_key) = rsa.newkeys(512)

    def encrypt(self, plaintext):
        """公開鍵で暗号化"""
        return rsa.encrypt(plaintext.encode("utf-8"), self.public_key)

    def decrypt(self, ciphertext):
        """秘密鍵で復号"""
        return rsa.decrypt(ciphertext, self.private_key).decode("utf-8")


rsa_cipher = RSAEncryption()
plaintext = "Hello, RSA!"
ciphertext = rsa_cipher.encrypt(plaintext)
print("Encrypted:", ciphertext)
decrypted_text = rsa_cipher.decrypt(ciphertext)
print("Decrypted:", decrypted_text)
