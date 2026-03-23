import hashlib

# Giả định đọc file
with open('shattered-1.pdf', 'rb') as f1, open('shattered-2.pdf', 'rb') as f2:
    hash1 = hashlib.sha1(f1.read()).hexdigest()
    hash2 = hashlib.sha1(f2.read()).hexdigest()
    print("Hash1:", hash1)
    print("Hash2:", hash2)
    print("Collision:", hash1 == hash2)