from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode


def encrypt(key, fn="sec.txt"):
    key = key.encode("utf-8")
    key = pad(key, AES.block_size)
    with open(fn, 'rb') as f, open(fn + ".enc", "w") as fout:
        data = f.read()
        cipher = AES.new(key, AES.MODE_CFB)
        cipher_text = cipher.encrypt(pad(data, AES.block_size))
        iv = b64encode(cipher.iv).decode("UTF-8")
        cipher_text = b64encode(cipher_text).decode("UTF-8")
        writing = iv + cipher_text
        fout.write(writing)
