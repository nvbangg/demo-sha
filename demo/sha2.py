import sys
import io

# Ép Terminal xuất ra định dạng UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import hashlib
import time

def find_collision(bit_length):
    hashes_found = {}
    attempts = 0
    start_time = time.time()
    
    # Số ký tự Hex cần lấy (1 ký tự Hex = 4 bit)
    hex_chars = bit_length // 4
    
    while True:
        attempts += 1
        # Tạo dữ liệu giả lập (chỉ cần số tăng dần là đủ)
        data = str(attempts).encode()
        full_hash = hashlib.sha256(data).hexdigest()
        short_hash = full_hash[:hex_chars]
        
        if short_hash in hashes_found:
            duration = time.time() - start_time
            return attempts, duration
        
        hashes_found[short_hash] = True

# Thử nghiệm với các độ khó tăng dần
print(f"{'Độ khó (Bit)':<15} | {'Số lần thử':<15} | {'Thời gian (s)':<15}")
print("-" * 50)

for bits in [12, 16, 20, 24]:
    attempts, duration = find_collision(bits)
    print(f"{bits:<15} | {attempts:<15,} | {duration:<15.4f}")