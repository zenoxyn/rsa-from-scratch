# 🔐 Implementasi RSA from Scratch

Implementasi algoritma **RSA (Rivest-Shamir-Adleman)** dari awal menggunakan Python murni tanpa library kriptografi eksternal. Proyek ini dibuat untuk tujuan edukasi dalam mata kuliah **Keamanan Data dan Informasi (KDI)**.

---

## 📚 Tentang RSA

**RSA** adalah salah satu algoritma kriptografi asimetris pertama yang cocok untuk enkripsi dan tanda tangan digital. Algoritma ini menggunakan sepasang kunci:

- **Public Key** (Kunci Publik) → untuk enkripsi
- **Private Key** (Kunci Privat) → untuk dekripsi

### Keamanan RSA

Keamanan RSA bergantung pada kesulitan **memfaktorkan bilangan besar** menjadi dua bilangan prima. Secara teori, siapa saja bisa memfaktorkan n, namun dalam praktik dengan bilangan yang sangat besar (2048-bit atau lebih), proses ini memakan waktu ribuan tahun.

---

## 🎯 Fitur

- ✅ Implementasi lengkap algoritma RSA dari nol
- ✅ Fungsi GCD (Greatest Common Divisor)
- ✅ Fungsi Modular Inverse
- ✅ Enkripsi dan Dekripsi pesan numerik
- ✅ Demonstrasi Key Generation
- ✅ Komentar dan dokumentasi lengkap

---

## 📋 Prasyarat

- Python 3.x
- Tidak memerlukan library tambahan (pure Python)

---

## 🚀 Cara Menjalankan

1. **Clone atau download** repository ini
2. **Buka terminal** di direktori proyek
3. **Jalankan** program:

```bash
python main.py
```

---

## 📖 Cara Kerja RSA

### 1️⃣ **Key Generation (Pembentukan Kunci)**

```
1. Pilih dua bilangan prima: p dan q
   Contoh: p = 7, q = 11

2. Hitung modulus: n = p × q
   n = 7 × 11 = 77

3. Hitung Euler's Totient: φ(n) = (p-1) × (q-1)
   φ(n) = (7-1) × (11-1) = 60

4. Pilih public exponent (e)
   Syarat: 1 < e < φ(n) dan gcd(e, φ(n)) = 1
   Contoh: e = 7

5. Hitung private exponent (d)
   Syarat: (d × e) mod φ(n) = 1
   d = 43

6. Hasil:
   - Public Key  = (e=7, n=77)
   - Private Key = (d=43, n=77)
```

### 2️⃣ **Encryption (Enkripsi)**

```
Rumus: C = M^e mod n

Contoh:
- Plaintext (M) = 9
- Public Key = (e=7, n=77)
- Ciphertext (C) = 9^7 mod 77 = 37
```

### 3️⃣ **Decryption (Dekripsi)**

```
Rumus: M = C^d mod n

Contoh:
- Ciphertext (C) = 37
- Private Key = (d=43, n=77)
- Plaintext (M) = 37^43 mod 77 = 9
```

---

## 💻 Contoh Output

```
===== KEY GENERATION =====
Public Key  : (7, 77)
Private Key : (43, 77)

===== ENCRYPTION =====
Plaintext  : 9
Ciphertext : 37

===== DECRYPTION =====
Decrypted Text : 9

Status : Dekripsi BERHASIL ✅
```

---

## 🔧 Struktur Kode

### **Fungsi Utama**

| Fungsi                   | Deskripsi                                                          |
| ------------------------ | ------------------------------------------------------------------ |
| `gcd(a, b)`              | Menghitung Greatest Common Divisor menggunakan algoritma Euclidean |
| `mod_inverse(e, phi)`    | Mencari modular multiplicative inverse (d) dari e modulo phi       |
| `encrypt(message, e, n)` | Mengenkripsi pesan menggunakan public key                          |
| `decrypt(cipher, d, n)`  | Mendekripsi ciphertext menggunakan private key                     |

### **Alur Program**

```
1. Key Generation → Membuat pasangan kunci public/private
2. Encryption     → Mengenkripsi plaintext menjadi ciphertext
3. Decryption     → Mendekripsi ciphertext kembali ke plaintext
4. Verification   → Memverifikasi hasil dekripsi
```

---

## 📐 Penjelasan Matematika

### **Greatest Common Divisor (GCD)**

Algoritma Euclidean untuk mencari FPB:

```
gcd(a, b):
    while b ≠ 0:
        temp = b
        b = a mod b
        a = temp
    return a
```

### **Modular Inverse**

Mencari d dimana `(d × e) mod φ(n) = 1`:

```
Contoh:
e = 7, φ(n) = 60
Cari d: (d × 7) mod 60 = 1
Jawaban: d = 43
Verifikasi: (43 × 7) mod 60 = 301 mod 60 = 1 ✅
```

### **Modular Exponentiation**

Python menggunakan `pow(base, exp, mod)` yang efisien:

```python
pow(9, 7, 77)  # = (9^7) mod 77 = 37
```

---

## 📝 Mengenkripsi String

Kode saat ini hanya mengenkripsi **bilangan bulat**. Untuk string, ada beberapa pendekatan:

### **Metode 1: Per Karakter**

```python
def encrypt_string(text, e, n):
    return [encrypt(ord(char), e, n) for char in text]

def decrypt_string(cipher_list, d, n):
    return ''.join([chr(decrypt(c, d, n)) for c in cipher_list])

# Contoh
pesan = "HELLO"
encrypted = encrypt_string(pesan, e, n)
decrypted = decrypt_string(encrypted, d, n)
```

### **Metode 2: Block Cipher**

Konversi beberapa karakter menjadi satu bilangan besar:

```python
def text_to_num(text):
    return int.from_bytes(text.encode(), 'big')

def num_to_text(num):
    return num.to_bytes((num.bit_length() + 7) // 8, 'big').decode()
```

**⚠️ Catatan:** Nilai numerik dari pesan harus **lebih kecil dari n**.

---

## ⚠️ Peringatan Keamanan

🚨 **Kode ini HANYA untuk tujuan EDUKASI!**

### **Jangan gunakan untuk produksi karena:**

1. ❌ **Bilangan prima terlalu kecil** (p=7, q=11)
   - Produksi memerlukan 1024-bit atau 2048-bit
2. ❌ **Modular inverse menggunakan brute force**
   - Terlalu lambat untuk bilangan besar
   - Seharusnya menggunakan Extended Euclidean Algorithm

3. ❌ **Tidak ada padding scheme**
   - Produksi memerlukan OAEP (Optimal Asymmetric Encryption Padding)

4. ❌ **Vulnerabel terhadap berbagai serangan**
   - Timing attack
   - Chosen ciphertext attack
   - Side-channel attack

### **Untuk Implementasi Produksi:**

Gunakan library yang sudah teruji:

- Python: `cryptography`, `PyCryptodome`
- Java: `java.security`
- JavaScript: `node-forge`, `crypto`

---

## 📚 Referensi

- [RSA (cryptosystem) - Wikipedia](<https://en.wikipedia.org/wiki/RSA_(cryptosystem)>)
- [The RSA Algorithm - Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/intro-to-rsa-encryption)
- Rivest, R.; Shamir, A.; Adleman, L. (1978). "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems"

---

## 👨‍💻 Author

**Mata Kuliah:** Keamanan Data dan Informasi (KDI)  
**Tujuan:** Demonstrasi edukatif algoritma RSA  
**Tanggal:** Maret 2026

---

## 📄 License

Proyek ini dibuat untuk keperluan edukasi. Gunakan dengan bijak! 🎓

---

## 🤝 Kontribusi

Jika ingin menambahkan fitur atau perbaikan:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/improvement`)
3. Commit perubahan (`git commit -m 'Add some feature'`)
4. Push ke branch (`git push origin feature/improvement`)
5. Buat Pull Request

---

## ❓ FAQ

### **Q: Mengapa menggunakan bilangan prima yang kecil?**

A: Untuk kemudahan pemahaman dan demonstrasi manual. Dalam praktik, gunakan bilangan prima 1024-bit atau lebih.

### **Q: Bagaimana cara enkripsi pesan yang panjang?**

A: Gunakan hybrid encryption (RSA + AES) atau bagi pesan menjadi blok-blok kecil.

### **Q: Apakah RSA masih aman di 2026?**

A: Ya, dengan key size 2048-bit atau lebih. Namun, quantum computing mengancam RSA di masa depan.

### **Q: Bisakah private key dihitung dari public key?**

A: Secara teori ya (dengan memfaktorkan n), tapi secara praktik tidak feasible untuk bilangan besar.

---

**⭐ Jika proyek ini membantu, berikan bintang di repository!**
