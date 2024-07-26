from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from tabulate import tabulate
import time

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
        encryption_data = EncryptionData(data_dict["apiKey"], data_dict["userUUID"], data_dict["sensitiveData"])

        # Step 4: Initialize an EncryptionConfiguration object using the user's UUID and the lengths of the salt and
        # cipher pools
        encryptionConf = EncryptionConfiguration(
            uuid_value=encryption_data.userUUID,
            salt_pool_size=general_salt_pool.__len__(),
            cipher_pool_size=general_cipher_pool.__len__()
        )
        print("::::::::::::::::::::::::New Request:::::::::::::::::::::::::::::::")

        # Step 5: Determine the indices for the cipher and salt methods
        cipher_index = encryptionConf.getCipherIndex()
        salt_index = encryptionConf.getSaltIndex()

        # Step 6: Print the request IP address, if available
        remote_addr = request.META.get('REMOTE_ADDR', 'Unknown')

        # Start timing the encryption process
        start_time = time.process_time()

        # Step 7: Encrypt the sensitive data using the selected cipher and salt methods
        encrypted_data = general_cipher_pool[cipher_index](
            encryption_data.sensitiveData, general_salt_pool[salt_index]
        )



        data = [
            ["Encryption Details"],
            ["Used Salt Value", "\033[92m{}\033[0m".format(general_salt_pool[salt_index])],
            ["Used Algorithm", "\033[92m" + general_cipher_pool[cipher_index].__name__ + "\033[0m"],
            ["Informed UUID", "\033[94m{}\033[0m".format(encryption_data.userUUID)],
            ["Informed Sensitive Data", "\033[94m{}\033[0m".format(encryption_data.sensitiveData)],
            ["Informed API Key", "\033[94m{}\033[0m".format(encryption_data.apiKey)],
            ["Selected Strategy", "\033[94mDefault Security Strategy\033[0m"],
            ["Requested IP Address", "\033[94m{}\033[0m".format(remote_addr)],
        ]

        # Print table
        print(tabulate(data, tablefmt="grid"))


        # Prepare the data to be returned as JSON
        response_data = {
            'encrypted_data': encrypted_data
        }

        # Return the encrypted data as an HTTP response in JSON format
        return JsonResponse(response_data)

    else:
        return HttpResponse("Only POST requests are accepted.")





