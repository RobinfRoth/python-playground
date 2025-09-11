#!/usr/bin/env python3

from secrets import token_bytes

def generate_random_key(n_bytes: int) -> int:
    """Generate a random key (bit string) of length ``n_bytes``."""
    tb: bytes = token_bytes(n_bytes)
    # convert bytes to bit string (int)
    return int.from_bytes(tb, "big")


def encrypt(original_data: str) -> tuple[int, int]:
    """Encrypt ``original_data`` using a one time pad. A pseudorandom
    key of the same length as the data is generated and used for
    encryption. It is returned along side the ``encrypted_data``.
    """
    original_bytes: bytes = original_data.encode()
    original_bit_string: int = int.from_bytes(original_bytes, "big")
    key: int = generate_random_key(len(original_bytes))

    encrypted_data: int = original_bit_string ^ key
    return encrypted_data, key


def decrypt(encrypted_data: int, key: int) -> str:
    """Decrypt the ``encrypted_data`` using ``key``. Both inputs need
    to use *big endian* byteorder.
    """
    decrypted_data: int = encrypted_data ^ key
    encrypted_length: int = (encrypted_data.bit_length() + 7) // 8

    return decrypted_data.to_bytes(encrypted_length, "big").decode()


if __name__ == "__main__":
    original = "Hello World!"
    enc, key = encrypt(original)

    print("Encrypted data:", enc)
    print("Key:", key)

    decrypted = decrypt(enc, key)
    print("Decrypted data:", decrypted)

    assert original == decrypted, (
        "Decrypted data does not match original data."
    )