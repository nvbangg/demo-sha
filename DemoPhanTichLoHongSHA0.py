import struct

def rol(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xffffffff

def expand_sha0(W):
    for i in range(16, 80):
        W.append(W[i-3] ^ W[i-8] ^ W[i-14] ^ W[i-16])
    return W

def expand_sha1(W):
    for i in range(16, 80):
        W.append(rol(W[i-3] ^ W[i-8] ^ W[i-14] ^ W[i-16], 1))
    return W

msg = b"ABCDEFGH"
msg = msg + b'\x80'
msg += b'\x00' * (56 - len(msg))
msg += struct.pack(">Q", len(msg)*8)

W0 = list(struct.unpack(">16I", msg[:64]))

W1 = W0.copy()
W2 = W0.copy()
W2[0] ^= 1

E1_sha0 = expand_sha0(W1.copy())
E2_sha0 = expand_sha0(W2.copy())

E1_sha1 = expand_sha1(W1.copy())
E2_sha1 = expand_sha1(W2.copy())

def count_diff(A, B):
    return sum(1 for x, y in zip(A, B) if x != y)

print("SHA-0 - số W[i] khác nhau:", count_diff(E1_sha0, E2_sha0))
print("SHA-1 - số W[i] khác nhau:", count_diff(E1_sha1, E2_sha1))