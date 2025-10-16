#bytes.fromhex() karena xor hanya bisa melakukan operasi pada integer bit atau bytes
k1 = bytes.fromhex("3c3f0193af37d2ebbc50cc6b91d27cf61197")
k21 = bytes.fromhex("ff76edcad455b6881b92f726987cbf30c68c")
k23 = bytes.fromhex("611568312c102d4d921f26199d39fe973118")
k1234 = bytes.fromhex("91ec5a6fa8a12f908f161850c591459c3887")
f45 = bytes.fromhex("0269dd12fe3435ea63f63aef17f8362cdba8")

def bxor(a, b):
    xor = (x ^ y for x, y in zip(a, b))
    return bytes(xor)

#mencari k4
# k1234 = k1 ^ k2 ^ k3 ^ k4
# k4 = k1234 ^ k1 ^ k2 ^ k3
# k4 = k1234 ^ k1 ^ k23
k4 = bxor(bxor(k1234, k1), k23)

#mencari f5
# f45 = flag ^ k4 ^ k5
# f5 = flag ^ k5 = flag ^ -k4- ^ k5 ^ -k4-
f5 = bxor(f45, k4)

#mencari k5
# k5 berupa 4-byte, berarti berkorespondensi dengan 4-byte awal pada f5
# karena flag format juga bagian dari flag, maka kita tahu kalau 4-byte awal pada flag adalah byte dari 'cry{'
# maka f5 = flag ^ k5
# k5 = f5 ^ flag
byteflag = b'cry{'
k5 = bxor(f5[:4], byteflag)

# setelah ditemukan k5 yang berupa 4-byte kita perlu membuat k5 dengan panjang yang sama
# panjangnya dengan byte yang ingin kita proses agar dapat melakukan operasi
k5 = (k5 * (len(f5) // len(k5)+1))[:len(f5)]

#mencari flag
# sekarang untuk mencari flag, kita tinggal melakukan xor pada f5 dengan k5 yang kita dapat
# flag = f5 ^ k5
flag = bxor(f5, k5)

#karena flag berupa bytes, maka untuk mengubahnya 
# menjadi string kita perlu .decode()
print(flag.decode())