import hashlib


def sha512_encrypt_version1(text):
    key = b'a5yCpD9F'
    mixed_text = str(text) + str(key)
    hashed_text = hashlib.sha512(mixed_text.encode()).hexdigest()
    return hashed_text


def sha512_encrypt_version2(text):
    key = b'dwEZDK8p'
    mixed_text = text + key
    hashed_text = hashlib.sha512(mixed_text.encode()).hexdigest()
    return hashed_text


def sha512_encrypt_version3(text):
    key = b'y7bKMqew'
    mixed_text = str(text) + str(key)
    hashed_text = hashlib.sha512(mixed_text.encode()).hexdigest()
    return hashed_text


def sha512_encrypt_version4(text):
    key = b'DVG7h6YC'
    mixed_text = str(text) + str(key)
    hashed_text = hashlib.sha512(mixed_text.encode()).hexdigest()
    return hashed_text


def sha512_encrypt_version5(text):
    key = b'Ca5UpsZr'
    mixed_text = str(text) + str(key)
    hashed_text = hashlib.sha512(mixed_text.encode()).hexdigest()
    return hashed_text
