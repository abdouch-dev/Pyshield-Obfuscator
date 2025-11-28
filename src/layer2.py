"""
This is the 2nd Layer of obfuscation
this one is for junk codes
"""
import random
import string

def add_junk_code(code, name):
    lines = f"{''.join(random.choice(string.ascii_letters) for i in range(random.randint(6,12)))} = '" + name * random.randint(10,15) + "'" + "\n" + code + "\n" + f"{''.join(random.choice(string.ascii_letters) for i in range(random.randint(6,12)))} = '" + name * random.randint(10,15) + "'"
    return lines