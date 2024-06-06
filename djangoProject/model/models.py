import json
from dataclasses import fields, dataclass

from django.db import models


@dataclass
class EncryptionData(object):
    apiKey: str
    userUUID: str
    sensitiveData: str

    @classmethod
    def from_json(cls, json_key):
        file = json.load(open("1.txt"))
        keys = [f.name for f in fields(cls)]
        # or: keys = cls.__dataclass_fields__.keys()
        json_data = file[json_key]
        normal_json_data = {key: json_data[key] for key in json_data if key in keys}
        anormal_json_data = {key: json_data[key] for key in json_data if key not in keys}
        tmp = cls(**normal_json_data)
        for anormal_key in anormal_json_data:
            setattr(tmp,anormal_key,anormal_json_data[anormal_key])
        return tmp