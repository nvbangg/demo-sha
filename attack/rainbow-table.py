import hashlib
import itertools

# Tạo rainbow table nhỏ cho password 1-3 ký tự (a-c để đơn giản)
alphabet = 'abc'
rainbow_table = {}
for length in range(1, 4):
    for attempt in itertools.product(alphabet, repeat=length):
        password = ''.join(attempt)
        hash_value = hashlib.sha1(password.encode()).hexdigest()
        rainbow_table[hash_value] = password

# Crack hash của "abc"
target_hash = hashlib.sha1(b"abc").hexdigest()
if target_hash in rainbow_table:
    print("Cracked password:", rainbow_table[target_hash])
else:
    print("Not found in table")