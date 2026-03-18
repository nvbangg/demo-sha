import hashlib
import itertools
import time

# Hash mục tiêu: SHA-1 của "abc"
target_hash = hashlib.sha1(b"abc").hexdigest()
print("Target SHA-1 hash:", target_hash)

# Brute-force: Thử password 1-4 ký tự (a-z)
start_time = time.time()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
found = False
for length in range(1, 5):
	for attempt in itertools.product(alphabet, repeat=length):
		password = ''.join(attempt)
		attempt_hash = hashlib.sha1(password.encode()).hexdigest()
		if attempt_hash == target_hash:
			print("Found password:", password)
			found = True
			break
	if found:
		break

end_time = time.time()
print("Time taken:", end_time - start_time, "seconds")