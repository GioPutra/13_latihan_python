import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # 1. Mengolah Data Menggunakan Pandas
    data_penjualan = {
        'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni'],
        'Total_Penjualan': [120, 150, 180, 200, 250, 310]
    }
    
    df = pd.DataFrame(data_penjualan)
    print("=== DATA PENJUALAN TOKO ===")
    print(df)
    print("---------------------------")

    # 2. Perhitungan Statistik Menggunakan NumPy
    penjualan_array = np.array(df['Total_Penjualan'])
    total = np.sum(penjualan_array)
    rata_rata = np.mean(penjualan_array)

    print(f"Total Penjualan : {total} unit")
    print(f"Rata-rata/Bulan : {rata_rata:.2f} unit")
    print("===========================\n")

    # 3. Visualisasi Data Menggunakan Matplotlib
    plt.figure(figsize=(8, 5))
    plt.plot(df['Bulan'], df['Total_Penjualan'], marker='o', color='b', linestyle='-', linewidth=2, label='Penjualan')
    
    plt.title('Grafik Penjualan Bulanan Toko', fontsize=14)
    plt.xlabel('Bulan', fontsize=12)
    plt.ylabel('Jumlah Penjualan (Unit)', fontsize=12)
    plt.grid(True)
    plt.legend()
    
    # Menampilkan grafik
    plt.show()

if __name__ == "__main__":
    main()