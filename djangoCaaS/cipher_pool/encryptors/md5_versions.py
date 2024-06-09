import hashlib


def md5_encrypt_version1(text):
    key = b'zdDf7M'
    mixed_text = text + key
    hashed_text = hashlib.md5(mixed_text.encode()).hexdigest()
    return hashed_text


def md5_encrypt_version2(text):
    key = b'Zbr5R3'
    mixed_text = text + key
    hashed_text = hashlib.md5(mixed_text.encode()).hexdigest()
    return hashed_text


def md5_encrypt_version3(text):
    key = b'Uj8hc2'
    mixed_text = text + key
    hashed_text = hashlib.md5(mixed_text.encode()).hexdigest()
    return hashed_text


def md5_encrypt_version4(text):
    key = b'MhCj9u'
    mixed_text = text + key
    hashed_text = hashlib.md5(mixed_text.encode()).hexdigest()
    return hashed_text


def md5_encrypt_version5(text):
    key = b'zeM7nX'
    mixed_text = text + key
    hashed_text = hashlib.md5(mixed_text.encode()).hexdigest()
    return hashed_text
