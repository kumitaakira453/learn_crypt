# 暗号化アルゴリズム集

このリポジトリには、いくつかの代表的な暗号化アルゴリズムの実装が含まれています。これらのアルゴリズムを使用して、データを暗号化および復号化する方法を学び、実際にコードとして体験できます。

## 目次

- [暗号化アルゴリズム集](#暗号化アルゴリズム集)
  - [目次](#目次)
  - [暗号化アルゴリズム](#暗号化アルゴリズム)
    - [AES 暗号](#aes-暗号)
    - [Caesar 暗号](#caesar-暗号)
    - [Vigenere 暗号](#vigenere-暗号)
    - [DES 暗号](#des-暗号)
    - [ECC 暗号](#ecc-暗号)
    - [RSA 暗号](#rsa-暗号)
  - [使い方](#使い方)
  - [依存関係](#依存関係)
  - [ライセンス](#ライセンス)

## 暗号化アルゴリズム

### AES 暗号

`aes_encryption.py` には、現代の強力な対称鍵暗号である **AES** (Advanced Encryption Standard) の実装が含まれています。AES は、128 ビット、192 ビット、または 256 ビットの鍵を使用してデータを暗号化します。ここでは、AES の基本的な暗号化および復号化機能を提供しています。

### Caesar 暗号

`caesar_cipher.py` は、シーザー暗号の実装です。この暗号では、各文字を指定された数だけシフトさせることで暗号化を行います。鍵はシフト数であり、単純な暗号化技法ですが、基本的な暗号化の概念を学ぶには役立ちます。

### Vigenere 暗号

`vigenere_cipher.py` には、**Vigenère 暗号** の実装があります。この暗号はシーザー暗号の改良版で、文字ごとに異なるシフトを使用するため、シーザー暗号よりもセキュリティが高いとされています。鍵を使用して、シフトのパターンを決定します。

### DES 暗号

`des_encryption.py` では、古典的な **DES** (Data Encryption Standard) 暗号の実装を行っています。DES はかつて広く使用されましたが、現在ではセキュリティ上の問題からほとんど使用されていません。ここでは、暗号化と復号化の基本的なメカニズムを学ぶことができます。

### ECC 暗号

`ecc_encryption.py` には、**ECC** (Elliptic Curve Cryptography) の実装があります。ECC は、楕円曲線を基にした暗号方式で、RSA よりも小さな鍵で同等のセキュリティを提供できるため、効率的な暗号化が可能です。ECC は、特にモバイルや IoT デバイスでの利用が増えています。

### RSA 暗号

`rsa_encryption.py` では、公開鍵暗号方式である **RSA** (Rivest-Shamir-Adleman) 暗号の実装を提供しています。RSA では、公開鍵と秘密鍵を用いてデータを暗号化および復号化します。RSA はセキュリティ業界で広く使われており、特にデジタル署名や鍵交換での使用が一般的です。

## 使い方

1. 各暗号化アルゴリズムのファイルを開き、コードを確認します。
2. 対象のアルゴリズムを使用したい場合、そのファイルをインポートして使用することができます。
3. 各ファイル内に、暗号化および復号化の例が含まれていますので、実際に試すことができます。

## 依存関係

このプロジェクトでは以下のパッケージが必要です：

- `pycryptodome` (AES、DES などの暗号化アルゴリズムに使用)
- `rsa` (RSA 暗号化に使用)

これらのパッケージは以下のコマンドでインストールできます：

```
pip install -r requirements.txt
```

## ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) のもとで提供されています。
