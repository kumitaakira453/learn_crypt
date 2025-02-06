class VigenereCipher:
    """ビジュネル暗号"""

    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        return self._vigenere_process(text, mode="encrypt")

    def decrypt(self, text):
        return self._vigenere_process(text, mode="decrypt")

    def _vigenere_process(self, text, mode="encrypt"):
        result = []
        key_index = 0
        for char in text:
            if char.isalpha():  # 英文字のみ対象
                base = ord("a") if char.islower() else ord("A")  # 小文字、大文字を区別
                alphabet_size = 26  # アルファベットの数
                key_char = self.key[key_index % len(self.key)]
                shift = ord(key_char.lower()) - ord("a")  # 鍵の文字をシフト量に変換
                if mode == "decrypt":
                    shift = -shift  # 複合化時はシフト方向を逆にする
                new_char = chr(
                    base + (ord(char) - base + shift) % alphabet_size
                )  # 新しい文字を計算
                result.append(new_char)
                key_index += 1  # 次の鍵の文字に進む
            else:
                result.append(char)  # 英字以外はそのまま
        return "".join(result)


# ヴィジュネル暗号の使用例
vigenere_cipher = VigenereCipher("KEY")
encrypted_vigenere = vigenere_cipher.encrypt("Hello World")
decrypted_vigenere = vigenere_cipher.decrypt(encrypted_vigenere)
print(f"Vigenere: {encrypted_vigenere} -> {decrypted_vigenere}")
