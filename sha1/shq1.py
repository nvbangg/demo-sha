import struct


def sha1_manual(data):
    # 1. Khởi tạo các biến hằng số (H0 - H4)
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Chuyển chuỗi sang mảng byte
    message = bytearray(data, 'utf-8')
    orig_len_in_bits = (len(message) * 8) & 0xffffffffffffffff

    # 2. Padding (Đệm dữ liệu)
    # Thêm bit 1 (0x80)
    message.append(0x80)
    # Thêm các bit 0 sao cho độ dài (L + 1 + k) chia 512 dư 448
    while len(message) % 64 != 56:
        message.append(0x00)

    # Thêm độ dài gốc của thông điệp (64-bit) vào cuối
    message += struct.pack('>Q', orig_len_in_bits)

    # 3. Xử lý theo từng khối 512-bit (64 bytes)
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        w = list(struct.unpack('>16L', chunk))

        # Mở rộng 16 từ ban đầu thành 80 từ
        for j in range(16, 80):
            val = w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16]
            # Phép dịch trái xoay vòng (Left Rotate) 1 bit
            w.append(((val << 1) | (val >> 31)) & 0xffffffff)

        # Khởi tạo giá trị băm cho khối này
        a, b, c, d, e = h0, h1, h2, h3, h4

        # 4. Vòng lặp chính (80 bước biến đổi)
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            # Phép dịch trái xoay vòng 5 bit cho 'a'
            temp = (((a << 5) | (a >> 27)) + f + e + k + w[j]) & 0xffffffff
            e = d
            d = c
            # Phép dịch trái xoay vòng 30 bit cho 'b'
            c = ((b << 30) | (b >> 2)) & 0xffffffff
            b = a
            a = temp

        # Cộng kết quả khối này vào giá trị tổng quát
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    # 5. Kết quả cuối cùng (Ghép các giá trị h lại thành chuỗi Hex)
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


# Chạy thử
test_str = "hello"
print(f"Chuỗi: {test_str}")
print(f"SHA1 thủ công: {sha1_manual(test_str)}")
