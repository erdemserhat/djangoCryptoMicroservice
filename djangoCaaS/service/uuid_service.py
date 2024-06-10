import random
import uuid


class EncryptionConfiguration:
    def __init__(
            self, uuid_value: str,
            cipher_pool_size: int,
            salt_pool_size: int):
        self.cipher_pool_size = cipher_pool_size
        self.uuid_value = uuid_value
        self.salt_pool_size = salt_pool_size

    def __generate_unique_index(self, limit: int) -> int:
        """
        Generate a random number within the range [0, limit] using the given UUID value.

        Parameters:
            limit (int): The upper bound of the range for the random number (inclusive).

        Returns:
            int: A random number within the range [0, limit].

        Explanation:
            This function generates a random number by using the provided UUID value. It processes
            the UUID value to create a normalized seed for the random number generator. The UUID is
            first processed by calculating the product of each character's ASCII value multiplied by
            its index in the UUID string. This product is then normalized by dividing it by the sum
            of the natural numbers up to the length of the UUID. The normalized value is used as a seed
            for the random number generator. Finally, a random integer within the specified range [0, limit]
            is generated and returned.
        """

        # Step 1: Calculate the total length of the UUID
        uuid_length = len(self.uuid_value)

        # Step 2: Calculate the product of each character's ASCII value multiplied by its index in the UUID string
        uuid_product = 0
        for i, char in enumerate(self.uuid_value):
            product = (i + 1) * ord(char)
            uuid_product += product

        # Step 3: Normalize the product by dividing it by the sum of the natural numbers up to the length of the UUID
        normalized_uuid_product = uuid_product / (uuid_length * (uuid_length + 1) / 2)

        # Step 4: Use the normalized UUID product as the seed for the random number generator
        random.seed(normalized_uuid_product)

        # Step 5: Generate a random integer within the specified range [0, limit)
        return random.randint(0, limit-1)

    def getSaltIndex(self) -> int:
        return self.__generate_unique_index(self.salt_pool_size)

    def getCipherIndex(self) -> int:
        return self.__generate_unique_index(self.cipher_pool_size)

