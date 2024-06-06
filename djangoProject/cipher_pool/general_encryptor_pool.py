from djangoProject.cipher_pool.encryptors.ecc_brainpoolp512r1_versions import encrypt_with_ecc_brainpoolp512r1_version1, \
    encrypt_with_ecc_brainpoolp512r1_version2, encrypt_with_ecc_brainpoolp512r1_version3, \
    encrypt_with_ecc_brainpoolp512r1_version4, encrypt_with_ecc_brainpoolp512r1_version5
from djangoProject.cipher_pool.encryptors.ecc_secp256r1_versions import encrypt_with_ecc_secp256r1_version1, \
    encrypt_with_ecc_secp256r1_version2, encrypt_with_ecc_secp256r1_version3, encrypt_with_ecc_secp256r1_version4, \
    encrypt_with_ecc_secp256r1_version5
from djangoProject.cipher_pool.encryptors.md5_versions import md5_encrypt_version1, md5_encrypt_version2, \
    md5_encrypt_version3, md5_encrypt_version4, md5_encrypt_version5
from djangoProject.cipher_pool.encryptors.sha1_versions import sha1_encrypt_version1, sha1_encrypt_version2, \
    sha1_encrypt_version3, sha1_encrypt_version4, sha1_encrypt_version5
from djangoProject.cipher_pool.encryptors.sha384_versions import sha384_encrypt_version1, sha384_encrypt_version2, \
    sha384_encrypt_version3, sha384_encrypt_version4, sha384_encrypt_version5
from djangoProject.cipher_pool.encryptors.sha512_versions import sha512_encrypt_version1, sha512_encrypt_version3, \
    sha512_encrypt_version4, sha512_encrypt_version2, sha512_encrypt_version5


general_cipher_pool = [

    # SHA256 POOL
    sha512_encrypt_version1,
    sha512_encrypt_version2,
    sha512_encrypt_version3,
    sha512_encrypt_version4,
    sha512_encrypt_version5,



    # CUSTOMIZED ECC BRAINPOOL512R1 POOL
    encrypt_with_ecc_brainpoolp512r1_version1,
    encrypt_with_ecc_brainpoolp512r1_version2,
    encrypt_with_ecc_brainpoolp512r1_version3,
    encrypt_with_ecc_brainpoolp512r1_version4,
    encrypt_with_ecc_brainpoolp512r1_version5,

    # CUSTOMIZED ECC SECP192R1 POOL
    encrypt_with_ecc_secp256r1_version1,
    encrypt_with_ecc_secp256r1_version2,
    encrypt_with_ecc_secp256r1_version3,
    encrypt_with_ecc_secp256r1_version4,
    encrypt_with_ecc_secp256r1_version5,

    # MD5 POOL
    md5_encrypt_version1,
    md5_encrypt_version2,
    md5_encrypt_version3,
    md5_encrypt_version4,
    md5_encrypt_version5,

    # SHA1 POOL
    sha1_encrypt_version1,
    sha1_encrypt_version2,
    sha1_encrypt_version3,
    sha1_encrypt_version4,
    sha1_encrypt_version5,

    # SHA384 POOL
    sha384_encrypt_version1,
    sha384_encrypt_version2,
    sha384_encrypt_version3,
    sha384_encrypt_version4,
    sha384_encrypt_version5,

    # SHA512 POOL
    sha512_encrypt_version1,
    sha512_encrypt_version2,
    sha512_encrypt_version3,
    sha512_encrypt_version4,
    sha512_encrypt_version5,





]
