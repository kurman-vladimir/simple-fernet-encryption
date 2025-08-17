import os
import base64

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


def _derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=720000,
    )
    key = kdf.derive(password.encode("ascii"))
    return base64.urlsafe_b64encode(key)


def encrypt(
    data: str,
    password: str,
) -> str:
    data_bytes = data.encode("ascii")
    salt = os.urandom(32)
    key = _derive_key(password, salt)
    token = Fernet(key).encrypt(data_bytes)

    parts = [
        base64.urlsafe_b64encode(salt).decode("ascii"),
        token.decode("ascii"),
    ]
    return "$".join(parts)


def decrypt(
    data: str,
    password: str,
) -> str:
    try:
        salt_b64, token_s = data.split("$", 1)
    except Exception as e:
        raise ValueError("wrong format") from e

    try:
        salt = base64.urlsafe_b64decode(salt_b64.encode("ascii"))
        token = token_s.encode("ascii")
    except Exception as e:
        raise ValueError("failed to encode") from e

    key = _derive_key(password, salt)
    try:
        plaintext = Fernet(key).decrypt(token)
    except Exception as e:
        raise ValueError("failed to decrypt") from e

    return plaintext.decode("ascii")
