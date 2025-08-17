from unittest import TestCase

from encryption import encrypt, decrypt


class EncryptionTests(TestCase):
    def test_encrypt(self) -> None:
        msg = "string to encrypt"
        pwd = "secure password"
        encrypted_msg = encrypt(msg, pwd)
        self.assertNotEqual(encrypted_msg, msg)
        decrypted_msg = decrypt(encrypted_msg, pwd)
        self.assertEqual(msg, decrypted_msg)
