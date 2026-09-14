import tkinter as tk
from tkinter import messagebox, ttk
import random

try:
    import inisiasi
except ImportError:
    inisiasi = None

# --- PALET WARNA & TEMA EDUKASI GALAKSI ---
SPACE_BG = "#030712"         # Hitam luar angkasa pekat
PANEL_BG = "#0b1329"         # Biru gelap panel kontrol
NEON_CYAN = "#00f3ff"        # Cyan terang / Hologram neon
NEON_PURPLE = "#a855f7"      # Ungu galaksi untuk aksen
TEXT_LIGHT = "#f8fafc"       # Putih kristal (Sangat mudah dibaca)
TEXT_MUTED = "#94a3b8"       # Abu-abu terang ramah mata
BTN_PRIMARY = "#2563eb"      # Biru cerah elegan, modern, tanpa garis tepi hitam
BTN_SUCCESS = "#059669"      # Hijau sistem aktif
BTN_DANGER = "#dc2626"       # Merah untuk keluar

class StarfieldCanvas(tk.Canvas):
    """Canvas latar belakang galaksi dengan bintang serta simbol matematika & geometri yang diperbesar lagi"""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg=SPACE_BG, highlightthickness=0, **kwargs)
        self.stars = []
        self.bind("<Configure>", self.create_stars)

    def create_stars(self, event):
        self.delete("star")
        self.stars.clear()
        width = event.width
        height = event.height
        
        math_symbols = ["1", "2", "3", "+", "-", "×", "÷", "△", "◯", "□", "π", "∑"]
        
        for _ in range(100):
            x = random.randint(0, width)
            y = random.randint(0, height)
            if random.random() > 0.45:
                size = random.choice([1, 1.5, 2, 2.5])
                color = random.choice([TEXT_LIGHT, NEON_CYAN, "#ffffff", "#93c5fd"])
                item = self.create_oval(x, y, x + size, y + size, fill=color, outline="", tags="star")
                self.stars.append((item, x, y))
            else:
                sym = random.choice(math_symbols)
                color = random.choice([NEON_CYAN, NEON_PURPLE, "#93c5fd", TEXT_MUTED])
                font_size = random.choice([16, 18, 20, 24])
                item = self.create_text(x, y, text=sym, fill=color, font=("Consolas", font_size, "bold"), tags="star")
                self.stars.append((item, x, y))


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Portal Belajar Interaktif - Matematika & Geometri untuk Semua")
        
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.resizable(True, True)

        if inisiasi:
            try:
                inisiasi.buat_database()
            except Exception:
                pass

        container = tk.Frame(self, bg=SPACE_BG)
        container.pack(fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginFrame, RegisterFrame, MainMenuFrame, BilanganFrame, BangunDatarFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class CosmicFrame(tk.Frame):
    def __init__(self, parent, controller, card_width=740, card_height=560):
        super().__init__(parent, bg=SPACE_BG)
        self.controller = controller
        
        self.canvas = StarfieldCanvas(self)
        self.canvas.pack(fill="both", expand=True)
        
        self.card = tk.Frame(self, bg=PANEL_BG, bd=2, relief="solid")
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=card_width, height=card_height)
        self.card.config(highlightbackground=NEON_CYAN, highlightcolor=NEON_CYAN, highlightthickness=1)


class LoginFrame(CosmicFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, card_width=720, card_height=540)
        
        tk.Label(self.card, text="✨ PORTAL EDUKASI MATEMATIKA & GEOMETRI ✨", font=("Consolas", 11, "bold"), bg=PANEL_BG, fg=NEON_CYAN).pack(pady=(25, 5))
        tk.Label(self.card, text="Selamat Datang di Ruang Belajar Interaktif", font=("Segoe UI", 18, "bold"), bg=PANEL_BG, fg=TEXT_LIGHT).pack(pady=(0, 5))
        tk.Label(self.card, text="Media belajar yang mudah dipahami oleh para pelajar.\nSilakan masuk untuk mulai mengeksplorasi angka dan bentuk ruang bersama!", font=("Segoe UI", 10), bg=PANEL_BG, fg=TEXT_MUTED, justify="center").pack(pady=(0, 20))

        form = tk.Frame(self.card, bg=PANEL_BG)
        form.pack(pady=5, padx=60, fill="x")

        tk.Label(form, text="NAMA PENGGUNA (USERNAME):", font=("Consolas", 9, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).pack(anchor="w")
        self.entry_user = tk.Entry(form, font=("Segoe UI", 11), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, relief="flat", bd=4)
        self.entry_user.pack(fill="x", pady=(3, 15), ipady=5)

        tk.Label(form, text="KATA SANDI (PASSWORD):", font=("Consolas", 9, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).pack(anchor="w")
        self.entry_pwd = tk.Entry(form, font=("Segoe UI", 11), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, show="*", relief="flat", bd=4)
        self.entry_pwd.pack(fill="x", pady=(3, 20), ipady=5)

        btn_frame = tk.Frame(self.card, bg=PANEL_BG)
        btn_frame.pack(pady=5, padx=60, fill="x")

        tk.Button(btn_frame, text="MASUK KE SISTEM BELAJAR", bg=BTN_PRIMARY, fg=TEXT_LIGHT, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.login).pack(fill="x", ipady=8, pady=(0, 10))
        
        sub_btn = tk.Frame(btn_frame, bg=PANEL_BG)
        sub_btn.pack(fill="x")
        tk.Button(sub_btn, text="Daftar Akun Baru", bg="#1e293b", fg=TEXT_LIGHT, font=("Segoe UI", 9), relief="flat", cursor="hand2", command=lambda: controller.show_frame("RegisterFrame")).pack(side=tk.LEFT, expand=True, fill="x", padx=(0, 5), ipady=5)
        tk.Button(sub_btn, text="Keluar Aplikasi", bg=BTN_DANGER, fg=TEXT_LIGHT, font=("Segoe UI", 9), relief="flat", cursor="hand2", command=controller.quit).pack(side=tk.RIGHT, expand=True, fill="x", padx=(5, 0), ipady=5)

    def login(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pwd.get().strip()
        if not user or not pwd:
            messagebox.showerror("Perhatian", "Nama pengguna dan kata sandi tidak boleh kosong!")
            return
        
        if inisiasi and inisiasi.cek_login(user, pwd):
            messagebox.showinfo("Berhasil", f"Selamat datang kembali, {user}! Mari belajar bersama.")
            self.entry_user.delete(0, tk.END)
            self.entry_pwd.delete(0, tk.END)
            self.controller.show_frame("MainMenuFrame")
        else:
            if not inisiasi:
                messagebox.showinfo("Simulasi", "Masuk berhasil! (Mode simulasi aktif)")
                self.controller.show_frame("MainMenuFrame")
            else:
                messagebox.showerror("Gagal", "Nama pengguna atau kata sandi salah!")


class RegisterFrame(CosmicFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, card_width=720, card_height=540)
        
        tk.Label(self.card, text="🚀 PENDAFTARAN PENGGUNA BARU", font=("Consolas", 11, "bold"), bg=PANEL_BG, fg=NEON_PURPLE).pack(pady=(25, 5))
        tk.Label(self.card, text="Bergabunglah dengan Komunitas Belajar Kami", font=("Segoe UI", 18, "bold"), bg=PANEL_BG, fg=TEXT_LIGHT).pack(pady=(0, 5))
        tk.Label(self.card, text="Buat akun pribadi Anda dengan mudah untuk mulai mengeksplorasi\nberbagai modul matematika dan geometri interaktif.", font=("Segoe UI", 10), bg=PANEL_BG, fg=TEXT_MUTED, justify="center").pack(pady=(0, 20))

        form = tk.Frame(self.card, bg=PANEL_BG)
        form.pack(pady=5, padx=60, fill="x")

        tk.Label(form, text="BUAT NAMA PENGGUNA:", font=("Consolas", 9, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).pack(anchor="w")
        self.entry_user = tk.Entry(form, font=("Segoe UI", 11), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, relief="flat", bd=4)
        self.entry_user.pack(fill="x", pady=(3, 15), ipady=5)

        tk.Label(form, text="BUAT KATA SANDI:", font=("Consolas", 9, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).pack(anchor="w")
        self.entry_pwd = tk.Entry(form, font=("Segoe UI", 11), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, show="*", relief="flat", bd=4)
        self.entry_pwd.pack(fill="x", pady=(3, 20), ipady=5)

        btn_frame = tk.Frame(self.card, bg=PANEL_BG)
        btn_frame.pack(pady=5, padx=60, fill="x")

        tk.Button(btn_frame, text="SIMPAN AKUN BARU", bg=BTN_SUCCESS, fg=TEXT_LIGHT, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.register).pack(fill="x", ipady=8, pady=(0, 10))
        tk.Button(btn_frame, text="Kembali ke Menu Masuk", bg="#1e293b", fg=TEXT_LIGHT, font=("Segoe UI", 9), relief="flat", cursor="hand2", command=lambda: controller.show_frame("LoginFrame")).pack(fill="x", ipady=5)

    def register(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pwd.get().strip()
        if not user or not pwd:
            messagebox.showerror("Perhatian", "Semua kolom pendaftaran harus diisi!")
            return
        
        if inisiasi and inisiasi.daftar_user(user, pwd):
            messagebox.showinfo("Sukses", "Akun berhasil dibuat! Silakan masuk dengan akun baru Anda.")
            self.entry_user.delete(0, tk.END)
            self.entry_pwd.delete(0, tk.END)
            self.controller.show_frame("LoginFrame")
        else:
            messagebox.showerror("Gagal", "Nama pengguna tersebut sudah terdaftar di sistem!")


class MainMenuFrame(CosmicFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, card_width=760, card_height=560)
        
        tk.Label(self.card, text="🌟 PUSAT PEMBELAJARAN UTAMA", font=("Consolas", 11, "bold"), bg=PANEL_BG, fg=NEON_CYAN).pack(pady=(30, 5))
        tk.Label(self.card, text="Pilih Modul Belajar yang Ingin Anda Eksplorasi", font=("Segoe UI", 18, "bold"), bg=PANEL_BG, fg=TEXT_LIGHT).pack(pady=(0, 5))
        tk.Label(self.card, text="Program ini dirancang khusus untuk membantu para pelajar\nmemahami konsep angka dan bentuk bangun datar dengan cara yang menyenangkan.", font=("Segoe UI", 10), bg=PANEL_BG, fg=TEXT_MUTED, justify="center").pack(pady=(0, 20))

        menu_box = tk.Frame(self.card, bg=PANEL_BG)
        menu_box.pack(pady=5, padx=50, fill="x")

        tk.Button(menu_box, text="✨  Cek Bilangan (Belajar Angka, Prima, Ganjil & Genap)", font=("Segoe UI", 11, "bold"), bg=BTN_PRIMARY, fg=TEXT_LIGHT, relief="flat", cursor="hand2", command=lambda: controller.show_frame("BilanganFrame")).pack(fill="x", ipady=14, pady=10)
        tk.Button(menu_box, text="📐  Kalkulator Bangun Datar (Hitung Luas & Keliling)", font=("Segoe UI", 11, "bold"), bg=BTN_PRIMARY, fg=TEXT_LIGHT, relief="flat", cursor="hand2", command=lambda: controller.show_frame("BangunDatarFrame")).pack(fill="x", ipady=14, pady=10)

        tk.Button(self.card, text="KELUAR / KEMBALI KE HALAMAN MASUK", font=("Segoe UI", 9, "bold"), bg=BTN_DANGER, fg=TEXT_LIGHT, relief="flat", cursor="hand2", width=35, command=lambda: controller.show_frame("LoginFrame")).pack(pady=(20, 0), ipady=6)


class BilanganFrame(CosmicFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, card_width=760, card_height=560)
        
        tk.Label(self.card, text="🔢 MODUL CEK BILANGAN & ANGKA", font=("Consolas", 11, "bold"), bg=PANEL_BG, fg=NEON_CYAN).pack(pady=(25, 5))
        tk.Label(self.card, text="Kenali Karakteristik Angka di Sekitar Kita", font=("Segoe UI", 18, "bold"), bg=PANEL_BG, fg=TEXT_LIGHT).pack(pady=(0, 5))
        tk.Label(self.card, text="Pilih jenis pemeriksaan di bawah ini untuk menguji apakah suatu angka\nmerupakan bilangan Prima, Ganjil, atau Genap dengan mudah.", font=("Segoe UI", 10), bg=PANEL_BG, fg=TEXT_MUTED, justify="center").pack(pady=(0, 15))

        self.pilihan = tk.StringVar(value="prima")
        
        radio_box = tk.Frame(self.card, bg=PANEL_BG)
        radio_box.pack(pady=10)
        
        r1 = tk.Radiobutton(radio_box, text="Cek Bilangan Prima", variable=self.pilihan, value="prima", bg=PANEL_BG, fg=TEXT_LIGHT, selectcolor="#1e293b", activebackground=PANEL_BG, activeforeground=NEON_CYAN, font=("Segoe UI", 11, "bold"), command=self.update_ui)
        r2 = tk.Radiobutton(radio_box, text="Cek Ganjil / Genap", variable=self.pilihan, value="ganjil_genap", bg=PANEL_BG, fg=TEXT_LIGHT, selectcolor="#1e293b", activebackground=PANEL_BG, activeforeground=NEON_CYAN, font=("Segoe UI", 11, "bold"), command=self.update_ui)
        r1.pack(side=tk.LEFT, padx=20)
        r2.pack(side=tk.LEFT, padx=20)

        self.frame_input = tk.Frame(self.card, bg=PANEL_BG)
        self.frame_input.pack(pady=25)

        self.update_ui()

        tk.Button(self.card, text="← Kembali ke Menu Utama", font=("Segoe UI", 10, "bold"), bg="#1e293b", fg=TEXT_LIGHT, relief="flat", cursor="hand2", width=30, command=lambda: controller.show_frame("MainMenuFrame")).pack(pady=(15, 0), ipady=7)

    def update_ui(self):
        for widget in self.frame_input.winfo_children():
            widget.destroy()

        choice = self.pilihan.get()
        tk.Label(self.frame_input, text="MASUKKAN ANGKA:", font=("Consolas", 10, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).pack(side=tk.LEFT, padx=10)
        self.entry_angka = tk.Entry(self.frame_input, font=("Segoe UI", 12), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, width=16, relief="flat", bd=5)
        self.entry_angka.pack(side=tk.LEFT, padx=10, ipady=5)

        if choice == "prima":
            tk.Button(self.frame_input, text="PERIKSA PRIMA", bg=BTN_SUCCESS, fg=TEXT_LIGHT, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.hitung_prima).pack(side=tk.LEFT, padx=10, ipady=6)
        else:
            tk.Button(self.frame_input, text="PERIKSA GANJIL/GENAP", bg=BTN_PRIMARY, fg=TEXT_LIGHT, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.hitung_ganjil_genap).pack(side=tk.LEFT, padx=10, ipady=6)

    def hitung_prima(self):
        try:
            n = int(self.entry_angka.get())
            if n <= 1:
                hasil = f"Angka {n} bukan bilangan prima."
            else:
                is_prima = True
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0:
                        is_prima = False
                        break
                hasil = f"Angka {n} adalah bilangan prima!" if is_prima else f"Angka {n} bukan bilangan prima."
            messagebox.showinfo("Hasil Pemeriksaan Bilangan", hasil)
        except ValueError:
            messagebox.showerror("Perhatian", "Harap masukkan angka bulat yang valid!")

    def hitung_ganjil_genap(self):
        try:
            n = int(self.entry_angka.get())
            hasil = f"Angka {n} adalah Bilangan Genap." if n % 2 == 0 else f"Angka {n} adalah Bilangan Ganjil."
            messagebox.showinfo("Hasil Pemeriksaan Bilangan", hasil)
        except ValueError:
            messagebox.showerror("Perhatian", "Harap masukkan angka bulat yang valid!")


class BangunDatarFrame(CosmicFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, card_width=780, card_height=600)
        
        tk.Label(self.card, text="📐 KALKULATOR BANGUN DATAR & RUANG", font=("Consolas", 11, "bold"), bg=PANEL_BG, fg=NEON_CYAN).pack(pady=(20, 5))
        tk.Label(self.card, text="Hitung Luas dan Keliling dengan Mudah", font=("Segoe UI", 18, "bold"), bg=PANEL_BG, fg=TEXT_LIGHT).pack(pady=(0, 5))
        tk.Label(self.card, text="Pilih bentuk geometri di bawah ini, lalu masukkan ukuran untuk menghitung\nluas dan keliling secara cepat dan akurat.", font=("Segoe UI", 10), bg=PANEL_BG, fg=TEXT_MUTED, justify="center").pack(pady=(0, 15))

        self.pilihan_bd = tk.StringVar(value="segitiga")
        
        radio_box = tk.Frame(self.card, bg=PANEL_BG)
        radio_box.pack(pady=8)
        
        for text, val in [("Segitiga", "segitiga"), ("Persegi", "persegi"), ("Persegi Panjang", "persegi_panjang"), ("Lingkaran", "lingkaran")]:
            tk.Radiobutton(radio_box, text=text, variable=self.pilihan_bd, value=val, bg=PANEL_BG, fg=TEXT_LIGHT, selectcolor="#1e293b", activebackground=PANEL_BG, activeforeground=NEON_CYAN, font=("Segoe UI", 10, "bold"), command=self.update_ui).pack(side=tk.LEFT, padx=10)

        self.frame_input = tk.Frame(self.card, bg=PANEL_BG)
        self.frame_input.pack(pady=20)

        self.update_ui()

        tk.Button(self.card, text="← Kembali ke Menu Utama", font=("Segoe UI", 10, "bold"), bg="#1e293b", fg=TEXT_LIGHT, relief="flat", cursor="hand2", width=30, command=lambda: controller.show_frame("MainMenuFrame")).pack(pady=(10, 0), ipady=7)

    def update_ui(self):
        for widget in self.frame_input.winfo_children():
            widget.destroy()

        choice = self.pilihan_bd.get()

        if choice == "segitiga":
            tk.Label(self.frame_input, text="ALAS (cm):", font=("Consolas", 10, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).grid(row=0, column=0, sticky="w", pady=6, padx=10)
            self.entry_alas = tk.Entry(self.frame_input, font=("Segoe UI", 11), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, width=22, relief="flat", bd=4)
            self.entry_alas.grid(row=0, column=1, pady=6, padx=10, ipady=4)

            tk.Label(self.frame_input, text="TINGGI (cm):", font=("Consolas", 10, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).grid(row=1, column=0, sticky="w", pady=6, padx=10)
            self.entry_tinggi = tk.Entry(self.frame_input, font=("Segoe UI", 11), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, width=22, relief="flat", bd=4)
            self.entry_tinggi.grid(row=1, column=1, pady=6, padx=10, ipady=4)

            tk.Button(self.frame_input, text="HITUNG LUAS SEGITIGA", bg=BTN_PRIMARY, fg=TEXT_LIGHT, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.hitung_segitiga).grid(row=2, columnspan=2, pady=15, ipady=6)

        elif choice == "persegi":
            tk.Label(self.frame_input, text="PANJANG SISI (cm):", font=("Consolas", 10, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).grid(row=0, column=0, sticky="w", pady=6, padx=10)
            self.entry_sisi = tk.Entry(self.frame_input, font=("Segoe UI", 11), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, width=22, relief="flat", bd=4)
            self.entry_sisi.grid(row=0, column=1, pady=6, padx=10, ipady=4)

            tk.Button(self.frame_input, text="HITUNG LUAS & KELILING", bg=BTN_PRIMARY, fg=TEXT_LIGHT, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.hitung_persegi).grid(row=1, columnspan=2, pady=20, ipady=6)

        elif choice == "persegi_panjang":
            tk.Label(self.frame_input, text="PANJANG (cm):", font=("Consolas", 10, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).grid(row=0, column=0, sticky="w", pady=6, padx=10)
            self.entry_panjang = tk.Entry(self.frame_input, font=("Segoe UI", 11), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, width=22, relief="flat", bd=4)
            self.entry_panjang.grid(row=0, column=1, pady=6, padx=10, ipady=4)

            tk.Label(self.frame_input, text="LEBAR (cm):", font=("Consolas", 10, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).grid(row=1, column=0, sticky="w", pady=6, padx=10)
            self.entry_lebar = tk.Entry(self.frame_input, font=("Segoe UI", 11), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, width=22, relief="flat", bd=4)
            self.entry_lebar.grid(row=1, column=1, pady=6, padx=10, ipady=4)

            tk.Button(self.frame_input, text="HITUNG LUAS & KELILING", bg=BTN_PRIMARY, fg=TEXT_LIGHT, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.hitung_persegi_panjang).grid(row=2, columnspan=2, pady=15, ipady=6)

        elif choice == "lingkaran":
            tk.Label(self.frame_input, text="JARI-JARI / r (cm):", font=("Consolas", 10, "bold"), bg=PANEL_BG, fg=TEXT_MUTED).grid(row=0, column=0, sticky="w", pady=6, padx=10)
            self.entry_jari = tk.Entry(self.frame_input, font=("Segoe UI", 11), bg="#020617", fg=TEXT_LIGHT, insertbackground=NEON_CYAN, width=22, relief="flat", bd=4)
            self.entry_jari.grid(row=0, column=1, pady=6, padx=10, ipady=4)

            tk.Button(self.frame_input, text="HITUNG LUAS & KELILING", bg=BTN_PRIMARY, fg=TEXT_LIGHT, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", command=self.hitung_lingkaran).grid(row=1, columnspan=2, pady=20, ipady=6)

    def hitung_segitiga(self):
        try:
            alas = float(self.entry_alas.get())
            tinggi = float(self.entry_tinggi.get())
            luas = 0.5 * alas * tinggi
            messagebox.showinfo("Hasil Perhitungan Geometri", f"Hasil Perhitungan Segitiga:\n• Luas = {luas} cm²")
        except ValueError:
            messagebox.showerror("Perhatian", "Harap masukkan angka yang valid!")

    def hitung_persegi(self):
        try:
            sisi = float(self.entry_sisi.get())
            luas = sisi * sisi
            keliling = 4 * sisi
            messagebox.showinfo("Hasil Perhitungan Geometri", f"Hasil Perhitungan Persegi:\n• Luas = {luas} cm²\n• Keliling = {keliling} cm")
        except ValueError:
            messagebox.showerror("Perhatian", "Harap masukkan angka yang valid!")

    def hitung_persegi_panjang(self):
        try:
            p = float(self.entry_panjang.get())
            l = float(self.entry_lebar.get())
            luas = p * l
            keliling = 2 * (p + l)
            messagebox.showinfo("Hasil Perhitungan Geometri", f"Hasil Perhitungan Persegi Panjang:\n• Luas = {luas} cm²\n• Keliling = {keliling} cm")
        except ValueError:
            messagebox.showerror("Perhatian", "Harap masukkan angka yang valid!")

    def hitung_lingkaran(self):
        try:
            r = float(self.entry_jari.get())
            luas = 3.14 * r * r
            keliling = 2 * 3.14 * r
            messagebox.showinfo("Hasil Perhitungan Geometri", f"Hasil Perhitungan Lingkaran:\n• Luas = {luas} cm²\n• Keliling = {keliling} cm")
        except ValueError:
            messagebox.showerror("Perhatian", "Harap masukkan angka yang valid!")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()