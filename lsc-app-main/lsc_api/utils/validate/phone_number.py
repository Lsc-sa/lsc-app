import re

def validate_phone_number(phone_number):
    phone_regex = r"^(?:\+?\d{1,3}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    if re.fullmatch(phone_regex, phone_number):
        return True
    return False