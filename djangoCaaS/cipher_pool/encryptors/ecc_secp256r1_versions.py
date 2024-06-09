from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend


def encrypt_with_ecc_secp256r1_version1(plaintext):
    key = "WbeQGLk32vPy6"
    mixed_text = plaintext + key
    private_key = ec.generate_private_key(
        ec.SECP256R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the text
    ciphertext = public_key.encrypt(
        mixed_text.encode(),
        ec.ECIES()
    )

    return ciphertext


def encrypt_with_ecc_secp256r1_version2(plaintext):
    key = "CMwYh6peZ7gQ5"
    mixed_text = plaintext + key
    private_key = ec.generate_private_key(
        ec.SECP256R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the text
    ciphertext = public_key.encrypt(
        mixed_text.encode(),
        ec.ECIES()
    )

    return ciphertext


def encrypt_with_ecc_secp256r1_version3(plaintext):
    key = "5fWH3VPZx4Ckj"
    mixed_text = plaintext + key
    private_key = ec.generate_private_key(
        ec.SECP256R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the text
    ciphertext = public_key.encrypt(
        mixed_text.encode(),
        ec.ECIES()
    )

    return ciphertext


def encrypt_with_ecc_secp256r1_version4(plaintext):
    key = "J63yg9nrHXLtw"
    mixed_text = plaintext + key
    private_key = ec.generate_private_key(
        ec.SECP256R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the text
    ciphertext = public_key.encrypt(
        mixed_text.encode(),
        ec.ECIES()
    )

    return ciphertext


def encrypt_with_ecc_secp256r1_version5(plaintext):
    key = "WUPxnARaQ4kB9"
    mixed_text = plaintext + key
    private_key = ec.generate_private_key(
        ec.SECP256R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the text
    ciphertext = public_key.encrypt(
        mixed_text.encode(),
        ec.ECIES()
    )

    return ciphertext
