import re


def email_verification(email):
    email = str(email).lower()
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    if not alphabet.isdisjoint(email):
        return False
    elif not "@" in email:
        return False
    elif not "." in email:
        return False

    result = True
    for item in email.split("@"):
        if len(item) < 2:
            result = False
            break

    if not result:
        return False

    else:
        return True


def phone_verification(phone):
    phone = re.sub(r'[^,0-9]', '', str(phone))
    if len(phone) != 11:
        return False

    if phone[0] != "7":
        return False

    return True


def full_name_verification(full_name):
    full_name = str(full_name).lower()
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя- ')
    if not alphabet.issuperset(full_name):
        return False

    if " " not in full_name:
        return False

    for item in full_name.split():
            if len(item) < 2:
                return False

    return True


def age_verification(age):
    try:
        int(age)
    except:
        return False

    if not 5 <= int(age) <= 120:
        return False
    return True

def city_verification(city):
    city = str(city).lower()
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя- ')
    if not alphabet.issuperset(city):
        return False
    if len(city) < 2:
        return False
    return True
