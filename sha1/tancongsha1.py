import hashlib

def sha1_file(path):
    with open(path, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()

file1 = "shattered-1.pdf"
file2 = "shattered-2.pdf"

h1 = sha1_file(file1)
h2 = sha1_file(file2)

print("SHA1 file 1:", h1)
print("SHA1 file 2:", h2)

if h1 == h2:
    print(">>> VA CHẠM SHA-1!")
else:
    print("Không va chạm")