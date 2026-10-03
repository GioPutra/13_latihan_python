import json
import sqlite3

# ==========================================
# 8.1 Saya dapat memakai list dan dictionary
# ==========================================
print("=== 8.1 LIST & DICTIONARY ===")
# Membuat dictionary data produk
produk_1 = {"id": 1, "nama": "Laptop", "harga": 7000000}
produk_2 = {"id": 2, "nama": "Mouse", "harga": 150000}

# Menyimpan dictionary ke dalam list
daftar_produk = [produk_1, produk_2]

# Menampilkan data dari list dan dictionary
for produk in daftar_produk:
    print(f"Produk: {produk['nama']} | Harga: Rp{produk['harga']}")


# ==========================================
# 8.2 Saya dapat membaca & menulis file
# ==========================================
print("\n=== 8.2 FILE HANDLING ===")
file_txt = "catatan.txt"

# Menulis ke file text (Write)
with open(file_txt, "w") as file:
    file.write("Ini adalah catatan sederhana.\nMenulis file berhasil!")

# Membaca file text (Read)
with open(file_txt, "r") as file:
    konten = file.read()
    print("Isi dari file txt:")
    print(konten)


# ==========================================
# 8.3 Saya dapat menyimpan & membaca data dengan JSON
# ==========================================
print("\n=== 8.3 FITUR JSON ===")
file_json = "data_produk.json"

# Menulis/Menyimpan data list & dictionary ke file JSON
with open(file_json, "w") as file:
    json.dump(daftar_produk, file, indent=4)
print("Data berhasil disimpan ke format JSON.")

# Membaca data dari file JSON
with open(file_json, "r") as file:
    data_terbaca = json.load(file)
    print("Hasil membaca file JSON:")
    print(data_terbaca)


# ==========================================
# 8.4 Saya dapat menyimpan & mengambil data dari database (INSERT, SELECT)
# ==========================================
print("\n=== 8.4 DATABASE SQLITE ===")

# Connecting/Membuat Database SQLite
conn = sqlite3.connect("toko.db")
cursor = conn.cursor()

# Membuat tabel jika belum ada
cursor.execute("""
    CREATE TABLE IF NOT EXISTS produk (
        id INTEGER PRIMARY KEY,
        nama TEXT NOT NULL,
        harga INTEGER NOT NULL
    )
""")

# 1. Menambah data (INSERT)
cursor.execute("INSERT OR REPLACE INTO produk (id, nama, harga) VALUES (1, 'Keyboard', 300000)")
cursor.execute("INSERT OR REPLACE INTO produk (id, nama, harga) VALUES (2, 'Monitor', 1500000)")
conn.commit()  # Menyimpan perubahan
print("Data berhasil dimasukkan (INSERT) ke Database.")

# 2. Mengambil data (SELECT)
cursor.execute("SELECT * FROM produk")
hasil_db = cursor.fetchall()

print("Hasil membaca data (SELECT) dari Database:")
for row in hasil_db:
    print(f"ID: {row[0]} | Nama: {row[1]} | Harga: Rp{row[2]}")

# Menutup koneksi database
conn.close()