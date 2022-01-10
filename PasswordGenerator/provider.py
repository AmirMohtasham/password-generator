import string
import random


def generate_password(length=10, use_upper=True, use_lower=True, use_number=True, use_punctuation=True):
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase

    if use_lower:
        chars += string.ascii_lowercase

    if use_number:
        chars += string.digits

    if use_punctuation:
        chars += string.punctuation

    return ''.join(random.choices(chars, k=length))
