class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        """テキストを暗号化"""
        return self._process_text(text, mode="encrypt")

    def decrypt(self, text):
        """複合"""
        return self._process_text(text, mode="decrypt")

    def _process_text(self, text, mode="encrypt"):
        """内部関数"""
        strResult = []

        for char in text:
            if char.isalpha():  # アルファベットのみ処理
                base = ord("a") if char.islower() else ord("A")
                alphabet_size = 26

                # モードに応じて処理
                if mode == "encrypt":
                    new_char = chr(base + (ord(char) - base + self.key) % alphabet_size)
                elif mode == "decrypt":
                    new_char = chr(base + (ord(char) - base - self.key) % alphabet_size)
                strResult.append(new_char)
            else:
                strResult.append(char)  # アルファベット以外の文字はそのまま

        return "".join(strResult)


caesar_cipher = CaesarCipher(3)
encrypted_caesar = caesar_cipher.encrypt("Hello World")
decrypted_caesar = caesar_cipher.decrypt(encrypted_caesar)
print(f"Caesar: {encrypted_caesar} -> {decrypted_caesar}")
