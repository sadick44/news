from cryptography.fernet import Fernet
from django.conf import settings


def encrypt_ids(id):
    try:

        encrypt_key = settings.encrypt_url_key
        id = str(id)

    except Exception as e:
        print(e)
