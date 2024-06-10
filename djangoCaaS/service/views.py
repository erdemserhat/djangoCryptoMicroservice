from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from djangoCaaS.cipher_pool.general_encryptor_pool import general_cipher_pool
from djangoCaaS.model.models import EncryptionData
from djangoCaaS.salt_pool.general_salt_pool import general_salt_pool
from service.uuid_service import EncryptionConfiguration


@csrf_exempt
def encrypt(request):
    """
    View function to handle encryption requests.

    This function processes POST requests containing sensitive data, user UUID, and an API key.
    It uses the provided UUID to determine the encryption and salt methods from predefined pools
    and returns the encrypted data as a response.

    Parameters:
        request (HttpRequest): The incoming HTTP request. Must be a POST request with JSON data.

    Returns:
        HttpResponse: The response containing encrypted data or an error message for non-POST requests.

    Detailed Steps:
    1. Check if the request method is POST.
    2. Parse the JSON data from the request body.
    3. Create an EncryptionData object using the parsed data.
    4. Initialize an EncryptionConfiguration object using the user's UUID and the lengths of the salt and cipher pools.
    5. Determine the indices for the cipher and salt methods.
    6. Encrypt the sensitive data using the selected cipher and salt methods.
    7. Return the encrypted data as an HTTP response.
    """

    if request.method == 'POST':

        # Step 2: Parse the JSON data from the request body
        json_data = request.body

        # Convert the JSON data to a dictionary
        data_dict = json.loads(json_data)

        # Step 3: Create an EncryptionData object using the parsed data
        my_object = EncryptionData(data_dict["apiKey"], data_dict["userUUID"], data_dict["sensitiveData"])

        # Step 4: Initialize an EncryptionConfiguration object using the user's UUID and the lengths of the salt and
        # cipher pools
        encryptionConf = EncryptionConfiguration(
            uuid_value=my_object.userUUID,
            salt_pool_size=general_salt_pool.__len__(),
            cipher_pool_size=general_cipher_pool.__len__()
        )

        # Step 5: Determine the indices for the cipher and salt methods
        cipher_index = encryptionConf.getCipherIndex()
        salt_index = encryptionConf.getSaltIndex()

        # Step 6: Encrypt the sensitive data using the selected cipher and salt methods
        encrypted_data = general_cipher_pool[cipher_index](
            my_object.sensitiveData, general_salt_pool[salt_index]
        )

        # Step 7: Return the encrypted data as an HTTP response
        return HttpResponse(encrypted_data)

    else:
        return HttpResponse("Only POST requests are accepted.")
