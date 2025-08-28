from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import sha256
import base64
class GiaiMa:
    @staticmethod
    def decrypt(encrypted_data: str, key_phrase: str, iv_base64: str) -> str:
        """Giải mã AES-256-CBC"""
        try:
            secret_key = sha256(key_phrase.encode()).digest()
            iv = base64.b64decode(iv_base64)
            decoded_data = base64.b64decode(encrypted_data)
            cipher = AES.new(secret_key, AES.MODE_CBC, iv)
            padded_data = cipher.decrypt(decoded_data)
            decrypted_data = unpad(padded_data, AES.block_size)
            return decrypted_data.decode('utf-8')
        except Exception as e:
            return f"Lỗi giải mã: {e}"
