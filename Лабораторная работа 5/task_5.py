import random
import string

random_digits = string.digits
random_letters_upper = string.ascii_uppercase
random_letters_lower = string.ascii_lowercase
alphabet = random_letters_upper + random_letters_lower + random_digits


def get_random_password() -> str:
    str_password = "".join(random.sample(alphabet, 8))

    return str_password


print(get_random_password())
