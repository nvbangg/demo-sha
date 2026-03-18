import hashlib

# Dữ liệu đầu vào
data = b"hello world"

# SHA-1 (gần giống SHA-0, SHA-0 có hash khác nhẹ do lỗi thiết kế)
sha1 = hashlib.sha1(data).hexdigest()

# SHA-2 (SHA-256 và SHA-512 làm ví dụ)
sha256 = hashlib.sha256(data).hexdigest()
sha512 = hashlib.sha512(data).hexdigest()

# SHA-3 (SHA3-256 và SHA3-512)
sha3_256 = hashlib.sha3_256(data).hexdigest()
sha3_512 = hashlib.sha3_512(data).hexdigest()

# In kết quả
print("SHA-1 hash:", sha1)
print("SHA-256 hash:", sha256)
print("SHA-512 hash:", sha512)
print("SHA3-256 hash:", sha3_256)
print("SHA3-512 hash:", sha3_512)

# Demo hash file: Tạo file mẫu và hash
with open('sample.txt', 'w') as f:
    f.write("This is a sample file for hashing.")

with open('sample.txt', 'rb') as f:
    file_data = f.read()
    file_sha256 = hashlib.sha256(file_data).hexdigest()
print("SHA-256 hash of sample file:", file_sha256)