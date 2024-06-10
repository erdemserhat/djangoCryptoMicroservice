from .encryptors.blake2b_versions import encrypt_with_blake2b_version1, encrypt_with_blake2b_version2, \
    encrypt_with_blake2b_version3, encrypt_with_blake2b_version4, encrypt_with_blake2b_version5
from .encryptors.blake2s_versions import encrypt_with_blake2s_version1, encrypt_with_blake2s_version2, \
    encrypt_with_blake2s_version3, encrypt_with_blake2s_version4, encrypt_with_blake2s_version5
from .encryptors.blake3_versions import encrypt_with_blake3_version1, encrypt_with_blake3_version2, \
    encrypt_with_blake3_version3, encrypt_with_blake3_version4, encrypt_with_blake3_version5
from .encryptors.md5_versions import encrypt_md5_version1, encrypt_md5_version2, encrypt_md5_version3, \
    encrypt_md5_version4, encrypt_md5_version5
from .encryptors.ripemd160_versions import encrypt_with_ripemd160_version1, encrypt_with_ripemd160_version2, \
    encrypt_with_ripemd160_version3, encrypt_with_ripemd160_version5, encrypt_with_ripemd160_version4
from .encryptors.sha128_versions import encrypt_with_sha128_version1, encrypt_with_sha128_version2, \
    encrypt_with_sha128_version3, encrypt_with_sha128_version4, encrypt_with_sha128_version5
from .encryptors.sha224_versions import encrypt_with_sha224_version1, encrypt_with_sha224_version2, \
    encrypt_with_sha224_version3, encrypt_with_sha224_version4, encrypt_with_sha224_version5
from .encryptors.sha256_versions import encrypt_with_sha256_version1, encrypt_with_sha256_version5, \
    encrypt_with_sha256_version4, encrypt_with_sha256_version3, encrypt_with_sha256_version2
from .encryptors.sha384_versions import encrypt_with_sha384_version1, encrypt_with_sha384_version2, \
    encrypt_with_sha384_version3, encrypt_with_sha384_version4, encrypt_with_sha384_version5
from .encryptors.sha512_versions import encrypt_with_sha512_version1, encrypt_with_sha512_version2, \
    encrypt_with_sha512_version3, encrypt_with_sha512_version4, encrypt_with_sha512_version5

general_cipher_pool = [
    encrypt_with_blake2b_version1,
    encrypt_with_blake2b_version2,
    encrypt_with_blake2b_version3,
    encrypt_with_blake2b_version4,
    encrypt_with_blake2b_version5,

    encrypt_with_blake2s_version1,
    encrypt_with_blake2s_version2,
    encrypt_with_blake2s_version3,
    encrypt_with_blake2s_version4,
    encrypt_with_blake2s_version5,

    encrypt_with_blake3_version1,
    encrypt_with_blake3_version2,
    encrypt_with_blake3_version3,
    encrypt_with_blake3_version4,
    encrypt_with_blake3_version5,

    encrypt_md5_version1,
    encrypt_md5_version2,
    encrypt_md5_version3,
    encrypt_md5_version4,
    encrypt_md5_version5,

    encrypt_with_ripemd160_version1,
    encrypt_with_ripemd160_version2,
    encrypt_with_ripemd160_version3,
    encrypt_with_ripemd160_version4,
    encrypt_with_ripemd160_version5,

    encrypt_with_sha128_version1,
    encrypt_with_sha128_version2,
    encrypt_with_sha128_version3,
    encrypt_with_sha128_version4,
    encrypt_with_sha128_version5,

    encrypt_with_sha224_version1,
    encrypt_with_sha224_version2,
    encrypt_with_sha224_version3,
    encrypt_with_sha224_version4,
    encrypt_with_sha224_version5,

    encrypt_with_sha256_version1,
    encrypt_with_sha256_version2,
    encrypt_with_sha256_version3,
    encrypt_with_sha256_version4,
    encrypt_with_sha256_version5,

    encrypt_with_sha384_version1,
    encrypt_with_sha384_version2,
    encrypt_with_sha384_version3,
    encrypt_with_sha384_version4,
    encrypt_with_sha384_version5,

    encrypt_with_sha512_version1,
    encrypt_with_sha512_version2,
    encrypt_with_sha512_version3,
    encrypt_with_sha512_version4,
    encrypt_with_sha512_version5,

]
