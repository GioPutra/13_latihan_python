# Fungsi segitiga
def segitiga(alas, tinggi):
    x = print("Luas segitiga:", 0.5 * alas * tinggi)
    y = print("Keliling segitiga:", alas + tinggi + (alas**2 + tinggi**2)**0.5)
    return x, y

# Fungsi persegi
def persegi(sisi):
    x = print("Luas persegi:", sisi * sisi)
    y = print("Keliling persegi:", 4 * sisi)
    return x, y

# Fungsi persegi panjang
def persegi_panjang(panjang, lebar):
    x = print("Luas persegi panjang:", panjang * lebar)
    y = print("Keliling persegi panjang:", 2 * (panjang + lebar))
    return x, y

# Fungsi lingkaran
def lingkaran(jari_jari):
    import math
    x = print("Luas Lingkaran:", math.pi * jari_jari ** 2)
    y = print("keliling Lingkaran:", 2 * math.pi * jari_jari)
    return x, y
