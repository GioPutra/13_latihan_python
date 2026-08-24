def cek_bilangan(angka):
    """Fungsi untuk menentukan apakah bilangan ganjil atau genap."""
    if angka % 2 == 0:
        return f"{angka} adalah bilangan genap 🟢"
    else:
        return f"{angka} adalah bilangan ganjil 🔴"

def main():
    """Fungsi utama untuk menjalankan perulangan dan menerima input pengguna."""
    print("<============ Program untuk menentukan GANJIL/GENAP ============>\n")

    while True:
        user_input = input("Masukkan bilangan yang akan diperiksa (atau ketik 'keluar'): ")

        # Mengecek jika pengguna ingin keluar langsung via teks
        if user_input.lower() == "keluar":
            print("Terima kasih telah menggunakan program ini.")
            print("================================================================")
            break

        # Validasi apakah input berupa angka positif/nol
        if user_input.isdigit():
            angka = int(user_input)
            hasil = cek_bilangan(angka)
            print(hasil)
            
            # Konfirmasi untuk melanjutkan perulangan
            lanjut = input("\nApakah ingin memeriksa bilangan lain? (Y/N): ").upper()
            if lanjut == "N":
                print("Terima kasih telah menggunakan program ini.")
                print("================================================================")
                break
            print()
        else:
            print("Input tidak valid. Masukkan angka yang benar atau ketik 'keluar'.\n")

if __name__ == "__main__":
    main()



    
