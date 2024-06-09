import hashlib


def sha1_encrypt_version1(text):
    key = b'RBp4rz9A'
    mixed_text = text + key
    hashed_text = hashlib.sha1(mixed_text.encode()).hexdigest()
    return hashed_text


def sha1_encrypt_version2(text):
    key = b'p8zhNqwH'
    mixed_text = text + key
    hashed_text = hashlib.sha1(mixed_text.encode()).hexdigest()
    return hashed_text


def sha1_encrypt_version3(text):
    key = b'mQey83fX'
    mixed_text = text + key
    hashed_text = hashlib.sha1(mixed_text.encode()).hexdigest()
    return hashed_text


def sha1_encrypt_version4(text):
    key = b'xG9gmw2F'
    mixed_text = text + key
    hashed_text = hashlib.sha1(mixed_text.encode()).hexdigest()
    return hashed_text


def sha1_encrypt_version5(text):
    key = b'RBp4rz9A'
    mixed_text = text + key
    hashed_text = hashlib.sha1(mixed_text.encode()).hexdigest()
    return hashed_text
