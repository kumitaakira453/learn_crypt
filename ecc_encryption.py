from ecdsa import SECP256k1, ecdsa
import base64


class ECCEncryption:
    def __init__(self):
        # SECP256k1楕円曲線を使用
        self.sk = ecdsa.SigningKey.generate(curve=SECP256k1)  # 秘密鍵
        self.pk = self.sk.get_verifying_key()  # 公開鍵

    def encrypt(self, plaintext):
        """ECCでは公開鍵を使って暗号化ではなく署名を行います"""
        signature = self.sk.sign(plaintext.encode("utf-8"))
        return base64.b64encode(signature).decode("utf-8")

    def decrypt(self, signature):
        """署名を検証して復号する"""
        signature = base64.b64decode(signature)
        try:
            self.pk.verify(signature, b"Hello, ECC!")
            return "Signature is valid."
        except ecdsa.BadSignatureError:
            return "Signature is invalid."


# 使用例
ecc_cipher = ECCEncryption()
plaintext = "Hello, ECC!"
signature = ecc_cipher.encrypt(plaintext)
print("Encrypted (Signature):", signature)
verification = ecc_cipher.decrypt(signature)
print("Verification:", verification)
