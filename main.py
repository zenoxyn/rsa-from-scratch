# ====================================
# IMPLEMENTASI RSA FROM SCRATCH
# Mata Kuliah : Keamanan Data dan Informasi
# Tujuan      : Demonstrasi proses RSA tanpa library kriptografi
# ====================================


# ------------------------------------------------
# Fungsi gcd (Greatest Common Divisor)
# Digunakan untuk mencari FPB dua bilangan
# menggunakan Algoritma Euclidean.
#
# Dalam RSA, nilai e harus relatif prima
# terhadap φ(n), artinya:
# gcd(e, φ(n)) = 1
# ------------------------------------------------
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# ------------------------------------------------
# Fungsi Modular Inverse
# Mencari nilai d sehingga:
#
#    (d * e) mod φ(n) = 1
#
# Nilai d ini menjadi PRIVATE KEY.
# Metode yang digunakan:
# brute force sederhana (mudah dipahami).
# ------------------------------------------------
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d


# ------------------------------------------------
# Fungsi Enkripsi RSA
#
# Rumus:
#    C = M^e mod n
#
# M : plaintext
# e : public exponent
# n : modulus
#
# pow(a,b,c) = (a^b) mod c (lebih efisien)
# ------------------------------------------------
def encrypt(message, e, n):
    return pow(message, e, n)


# ------------------------------------------------
# Fungsi Dekripsi RSA
#
# Rumus:
#    M = C^d mod n
#
# C : ciphertext
# d : private key
# n : modulus
# ------------------------------------------------
def decrypt(cipher, d, n):
    return pow(cipher, d, n)


# =================================================
#              KEY GENERATION
# =================================================

# Step 1: memilih dua bilangan prima
# (contoh kecil agar mudah dihitung)
p = 7
q = 11

# Step 2: menghitung modulus n
# n digunakan pada public dan private key
n = p * q

# Step 3: menghitung Euler Totient Function
# φ(n) = (p-1)(q-1)
phi = (p - 1) * (q - 1)

# Step 4: memilih public exponent (e)
# harus relatif prima terhadap φ(n)
e = 7

# Step 5: menghitung private key (d)
d = mod_inverse(e, phi)

# Menampilkan pasangan kunci
print("===== KEY GENERATION =====")
print("Public Key  :", (e, n))
print("Private Key :", (d, n))


# =================================================
#                  ENCRYPTION
# =================================================

# Plaintext (pesan asli)
message = 9

# Proses enkripsi menggunakan public key
cipher = encrypt(message, e, n)

print("\n===== ENCRYPTION =====")
print("Plaintext  :", message)
print("Ciphertext :", cipher)


# =================================================
#                  DECRYPTION
# =================================================

# Proses dekripsi menggunakan private key
original = decrypt(cipher, d, n)

print("\n===== DECRYPTION =====")
print("Decrypted Text :", original)


# =================================================
# Verifikasi
# Jika RSA berjalan benar:
# plaintext awal == hasil dekripsi
# =================================================
if message == original:
    print("\nStatus : Dekripsi BERHASIL ✅")
else:
    print("\nStatus : Dekripsi GAGAL ❌")