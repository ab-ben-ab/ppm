from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import getpass

def decrypt():
    key = getpass.getpass("password: ").encode("UTF-8")
    key = pad(key, AES.block_size)

    with open("sec.txt.enc", "r") as f, open("sec.txt", "wb") as fout:
        try:
            data = f.read()
            iv = b64decode(data[:24])
            cipher_text = b64decode(data[24:])
            cipher = AES.new(key, AES.MODE_CFB, iv)
            decrypted = unpad(cipher.decrypt(cipher_text), AES.block_size)
            fout.write(decrypted)
        except Exception:
            print("wrong password")
