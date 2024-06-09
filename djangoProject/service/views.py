from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from djangoProject.cipher_pool.general_encryptor_pool import general_cipher_pool
from djangoProject.model.models import EncryptionData
from djangoProject.salt_pool.general_salt_pool import general_salt_pool


def hello_world(request):
    return HttpResponse('Hello, World!')


@csrf_exempt
def encrypt(request):
    if request.method == 'POST':
        # Form verilerine erişmek için request.POST kullanılır
        json_data = request.body
        # JSON verisi

        # JSON verisini bir sözlüğe dönüştürme
        data_dict = json.loads(json_data)

        # Sözlüğü kullanarak sınıf nesnesi oluşturma
        my_object = EncryptionData(data_dict["apiKey"], data_dict["userUUID"], data_dict["sensitiveData"])

        #

        print(general_cipher_pool[3](my_object.sensitiveData))

        # validate API KEY

        return HttpResponse("POST request alındı ve işlendi.")
    else:
        return HttpResponse("Sadece POST istekleri kabul edilir.")
