from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend


def encrypt_with_ecc_brainpoolp512r1_version1(plaintext):
    key = "Jj3Ush82Hw5vg"
    mixedText = plaintext + key
    private_key = ec.generate_private_key(
        ec.BrainpoolP512R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Metni şifrele
    ciphertext = public_key.encrypt(
        mixedText,
        ec.SECP192R1
    )

    return ciphertext


def encrypt_with_ecc_brainpoolp512r1_version2(plaintext):
    key = "3hPTsdWjf9L2m"
    mixedText = plaintext + key
    private_key = ec.generate_private_key(
        ec.BrainpoolP512R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Metni şifrele
    ciphertext = public_key.encrypt(
        mixedText,
        ec.SECP192R1()
    )

    return ciphertext


def encrypt_with_ecc_brainpoolp512r1_version3(plaintext):
    key = "2qTG9XvuMnS7L"
    mixedText = plaintext + key
    private_key = ec.generate_private_key(
        ec.BrainpoolP512R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Metni şifrele
    ciphertext = public_key.encrypt(
        mixedText,
        ec.SECP192R1()
    )

    return ciphertext


def encrypt_with_ecc_brainpoolp512r1_version4(plaintext):
    key = "Zg4pSEh35VA9y"
    mixedText = plaintext + key
    private_key = ec.generate_private_key(
        ec.BrainpoolP512R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Metni şifrele
    ciphertext = public_key.encrypt(
        mixedText,
        ec.SECP192R1()
    )

    return ciphertext


def encrypt_with_ecc_brainpoolp512r1_version5(plaintext):
    key = "UHjxP5ev8zL4c"
    mixedText = plaintext + key
    private_key = ec.generate_private_key(
        ec.BrainpoolP512R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Metni şifrele
    ciphertext = public_key.encrypt(
        mixedText,
        ec.SECP192R1()
    )

    return ciphertext
