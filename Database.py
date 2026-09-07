import os
import inisiasi
import ModulMatematika as math
import ModulBangunDatar as bd

def clear_screen():
    os.system("cls")

# 1. Otomatis buat database
inisiasi.buat_database()

# 2. SESI LOGIN / REGISTER
clear_screen()
while True:
    print("==================================================")
    print("          SYSTEM AUTHENTICATION USER              ")
    print("==================================================")
    print("1. Login")
    print("2. Buat Akun Baru (Register)")
    print("3. Keluar")
    pilih_auth = input("Pilihan Anda (1/2/3): ")

    if pilih_auth == "1":
        user = input("Masukkan Username: ")
        pwd = input("Masukkan Password: ")
        if inisiasi.cek_login(user, pwd):
            print(f"\n[+] Login Berhasil! Selamat datang, {user}.\n")
            input("Tekan Enter untuk masuk ke Program Utama...")
            clear_screen()
            break  # Lanjut ke program utama di bawah
        else:
            print("\n[-] Username atau password salah!\n")

    elif pilih_auth == "2":
        user = input("Buat Username Baru: ")
        pwd = input("Buat Password Baru: ")
        if inisiasi.daftar_user(user, pwd):
            print("\n[+] Akun berhasil dibuat! Silakan Login.\n")
        else:
            print("\n[-] Username sudah terdaftar!\n")

    elif pilih_auth == "3":
        exit()

# 3. PROGRAM UTAMA (Matematika & Bangun Datar)
while True:
    print("<============ SELAMAT DATANG PADA PROGRAM BANGUN DATAR/BILANGAN ============>\n")
    program = input("Masukan Program yang ingin dijalankan\n Check Bilangan = 1\n Check Bangun Datar = 2\n Pilihan Anda: ")
    
    if program == "1":
        program_mat = input("Check Bilangan Prima = 1\n Check Bilangan Ganjil/Genap = 2\n Pilihan Anda: ")
        if program_mat == "1":
            math.prima()
        elif program_mat == "2":
            math.ganjil_genap()
            
    elif program == "2":
        program_bd = input("Check Nilai Segitiga = 1\n Check Nilai Persegi = 2\n Check Nilai Persegi Panjang = 3\n Check Nilai Lingkaran = 4\n Pilihan Anda: ")
        if program_bd == "1":
            bd.segitiga()
        elif program_bd == "2":
            bd.persegi()
        elif program_bd == "3":
            bd.persegi_panjang()
        elif program_bd == "4":
            bd.lingkaran()