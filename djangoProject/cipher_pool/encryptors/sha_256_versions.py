import hashlib


def sha256_encrypt_version1(text):
    key = b'SHj2y5'
    mixed_text = text + key
    hashed_text = hashlib.sha256(mixed_text.encode()).hexdigest()
    return hashed_text


def sha256_encrypt_version2(text):
    key = b'VPw5Q6'
    mixed_text = text + key
    hashed_text = hashlib.sha256(mixed_text.encode()).hexdigest()
    return hashed_text


def sha256_encrypt_version3(text):
    key = b'L9Eftx'
    mixed_text = text + key
    hashed_text = hashlib.sha256(mixed_text.encode()).hexdigest()
    return hashed_text


def sha256_encrypt_version4(text):
    key = b'Q7UXcf'
    mixed_text = text + key
    hashed_text = hashlib.sha256(mixed_text.encode()).hexdigest()
    return hashed_text


def sha256_encrypt_version5(text):
    key = b'ck7Wd4'
    mixed_text = text + key
    hashed_text = hashlib.sha256(mixed_text.encode()).hexdigest()
    return hashed_text
