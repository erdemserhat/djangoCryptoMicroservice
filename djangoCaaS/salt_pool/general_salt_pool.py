from djangoCaaS.salt_pool.salts.salt_pool_length12_versions import salt_pool_length12
from djangoCaaS.salt_pool.salts.salt_pool_length16_versions import salt_pool_length16
from djangoCaaS.salt_pool.salts.salt_pool_length8_versions import salt_pool_length8

general_salt_pool = []
general_salt_pool.extend(salt_pool_length8)
general_salt_pool.extend(salt_pool_length12)
general_salt_pool.extend(salt_pool_length16)


