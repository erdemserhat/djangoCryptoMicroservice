import hashlib


def sha384_encrypt_version1(text):
    key = b'RwpEd5Fb'
    mixed_text = text + key
    hashed_text = hashlib.sha384(mixed_text.encode()).hexdigest()
    return hashed_text


def sha384_encrypt_version2(text):
    key = b'p9SBrYg6'
    mixed_text = text + key
    hashed_text = hashlib.sha384(mixed_text.encode()).hexdigest()
    return hashed_text


def sha384_encrypt_version3(text):
    key = b'YwWV5RuF'
    mixed_text = text + key
    hashed_text = hashlib.sha384(mixed_text.encode()).hexdigest()
    return hashed_text


def sha384_encrypt_version4(text):
    key = b'HMX5SFnk'
    mixed_text = text + key
    hashed_text = hashlib.sha384(mixed_text.encode()).hexdigest()
    return hashed_text


def sha384_encrypt_version5(text):
    key = b'XhS365q4'
    mixed_text = text + key
    hashed_text = hashlib.sha384(mixed_text.encode()).hexdigest()
    return hashed_text
