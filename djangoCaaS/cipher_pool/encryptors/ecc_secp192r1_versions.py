from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend


def encrypt_with_ecc_secp192r1_version1(plaintext):
    key = "RfnEXwQd6pcU2"
    mixed_text = plaintext + key
    private_key = ec.generate_private_key(
        ec.SECP192R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the text
    ciphertext = public_key.encrypt(
        mixed_text.encode(),
        ec.ECIES()
    )

    return ciphertext


def encrypt_with_ecc_secp192r1_version2(plaintext):
    key = "6VKZ8XLGRgQAY"
    mixed_text = plaintext + key
    private_key = ec.generate_private_key(
        ec.SECP192R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the text
    ciphertext = public_key.encrypt(
        mixed_text.encode(),
        ec.ECIES()
    )

    return ciphertext


def encrypt_with_ecc_secp192r1_version3(plaintext):
    key = "dVB9un6zDCXAe"
    mixed_text = plaintext + key
    private_key = ec.generate_private_key(
        ec.SECP192R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the text
    ciphertext = public_key.encrypt(
        mixed_text.encode(),
        ec.ECIES()
    )

    return ciphertext


def encrypt_with_ecc_secp192r1_version4(plaintext):
    key = "rXxe93BWTpf8g"
    mixed_text = plaintext + key
    private_key = ec.generate_private_key(
        ec.SECP192R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the text
    ciphertext = public_key.encrypt(
        mixed_text.encode(),
        ec.ECIES()
    )

    return ciphertext


def encrypt_with_ecc_secp192r1_version5(plaintext):
    key = "tCJ2QcAMkR7xu"
    mixed_text = plaintext + key
    private_key = ec.generate_private_key(
        ec.SECP192R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the text
    ciphertext = public_key.encrypt(
        mixed_text.encode(),
        ec.ECIES()
    )

    return ciphertext
