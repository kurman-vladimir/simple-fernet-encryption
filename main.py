import argparse

from encryption import encrypt, decrypt


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("data", help="Data to encrypt or decrypt")
    parser.add_argument("--encryption-key", required=True, help="Encryption key")
    args = parser.parse_args()
    match args.action:
        case "encrypt":
            encrypted_data = encrypt(args.data, args.encryption_key)
            decrypted_data = decrypt(encrypted_data, args.encryption_key)
            if decrypted_data != args.data:
                raise ValueError("Decrypted data does not match original data")
            print(f"Encrypted data: {encrypted_data}")
        case "decrypt":
            decrypted_data = decrypt(args.data, args.encryption_key)
            print(f"Decrypted data: {decrypted_data}")
        case _:
            raise ValueError("Invalid action specified")
