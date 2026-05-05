import random
import string

from .models import Url

def create_short_code(length=6):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        short_code = ''.join(random.choices(all_chars, k=length))

        if not Url.objects.filter(short_code=short_code).exists():
            return short_code
