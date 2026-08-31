import os
import ModulMatematika as math
import ModulBangunDatar as bd
def clear_screen():
    os.system("cls")

clear_screen()

while True:
    print("<============ SELAMAT DATANG PADA PROGRAM BANGUN DATAR/BILANGAN ============>\n")
    program = input("Masukan Program yang ingin dijalankan\n Check Bilangan = 1\n Check Bangun Datar = 2\n Pilihan Anda: ")
    if program == "1":
        print("<============ Program Matematika ============>\n")
        program_mat = input("Masukan Program yang ingin dijalankan\n Check Bilangan Prima = 1\n Check Bilangan Ganjil/Genap = 2\n Pilihan Anda: ")
        if program_mat == "1":
            math.prima()
        elif program_mat == "2":
            math.ganjil_genap()
        else:
            print("Program tidak dikenal.")
            break
    elif program == "2":
        print("<============ Program Bangun Datar ============>\n")
        program_bd = input("Masukan Program yang ingin dijalankan\n Check Nilai Segitiga = 1\n Check Nilai Persegi = 2\n Check Nilai Persegi Panjang = 3\n Check NilaiLingkaran = 4\n Pilihan Anda: ")
        if program_bd == "1":
            bd.segitiga()
        elif program_bd == "2":
            bd.persegi()
        elif program_bd == "3":
            bd.persegi_panjang()
        elif program_bd == "4":
            bd.lingkaran()
        else:
            print("Program tidak dikenal.")
            break
        
