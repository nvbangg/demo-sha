import struct
import hashlib

# ===== Server =====
secret = b"key123"
message = b"user=guest"

def mac(msg):
    return hashlib.sha256(secret + msg).hexdigest()

original_msg = message
original_hash = mac(original_msg)

print("Original hash:", original_hash)

# ===== Attacker =====
append = b"&admin=true"
secret_len = 6  # đoán

# ===== Hàm tạo padding chuẩn SHA-256 =====
def sha256_padding(msg_len):
    padding = b'\x80'
    padding += b'\x00' * ((56 - (msg_len + 1) % 64) % 64)
    padding += struct.pack('>Q', msg_len * 8)
    return padding

# tổng độ dài (secret + message)
total_len = secret_len + len(original_msg)

padding = sha256_padding(total_len)

# message mới attacker gửi
new_msg = original_msg + padding + append

print("New message:", new_msg)