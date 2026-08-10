print("<============ Program untuk menentukan GANJIL/GENAP ============>")
while True:
    x = int(input("Masukkan bilangan yang akan diperiksa: "))

    if x % 2 == 0:
        print(x, "adalah bilangan genap 🟢")
    else:
        print(x, "adalah bilangan ganjil 🔴")
        
    if input("\nApakah ingin memeriksa bilangan lain? (Y/N):").upper() == "N":
        print("Terima kasih telah menggunakan program ini.")
        print("================================================================")
        break
    else:
        continue