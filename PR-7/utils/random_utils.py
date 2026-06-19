import random
import string

def random_number(start, end):
    return random.randint(start, end)

def random_list(size, start, end):
    return [random.randint(start, end) for _ in range(size)]

def random_password(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def random_otp():
    return random.randint(100000, 999999)