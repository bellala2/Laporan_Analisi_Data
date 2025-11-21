# ============================================================
# LANGKAH 1 – IMPORT LIBRARY
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# LANGKAH 2 – IMPORT DATA CSV
# ============================================================
df = pd.read_csv("Data_Penjualan_Toko_Online.csv")
print("5 Data Teratas:")
print(df.head())

# ============================================================
# LANGKAH 3 – CEK DAN MEMBERSIHKAN DATA
# ============================================================
print("\nInformasi Dataset:")
print(df.info())

print("\nJumlah Null:")
print(df.isnull().sum())

# Menghapus baris yang memiliki nilai kosong
df = df.dropna()

# ============================================================
# LANGKAH 4 – ANALISIS DESKRIPTIF
# ============================================================
print("\nStatistik Deskriptif:")
print(df.describe())

print("\nProduk Terlaris (berdasarkan jumlah penjualan):")
print(df.groupby("Produk")["Jumlah"].sum().sort_values(ascending=False))

# ============================================================
# LANGKAH 5 – VISUALISASI DATA
# ============================================================

# Grafik Bar Total Pendapatan per Produk
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Produk", y="Pendapatan", estimator=sum, ci=None)
plt.title("Total Pendapatan per Produk")
plt.xlabel("Produk")
plt.ylabel("Total Pendapatan")
plt.show()

# Grafik Line Tren Pendapatan Mingguan
plt.figure(figsize=(10,5))
sns.lineplot(data=df, x="Tanggal", y="Pendapatan", marker="o")
plt.title("Tren Pendapatan Mingguan")
plt.xlabel("Tanggal")
plt.ylabel("Pendapatan")
plt.show()

# ============================================================
# LANGKAH 6 – SIMPAN HASIL ANALISIS
# ============================================================
df.to_csv("hasil_analisis_penjualan.csv", index=False)
print("\nData hasil analisis telah disimpan sebagai: hasil_analisis_penjualan.csv")

# ============================================================
# E. PRAKTIK MANDIRI
# ============================================================

# Tambahkan kolom Diskon (10%)
df["Diskon"] = 0.10   # 10%

# Hitung Pendapatan Bersih
df["Pendapatan Bersih"] = df["Pendapatan"] - (df["Pendapatan"] * df["Diskon"])

# Grafik Bar Pendapatan Bersih per Produk
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Produk", y="Pendapatan Bersih", estimator=sum, ci=None)
plt.title("Pendapatan Bersih per Produk")
plt.xlabel("Produk")
plt.ylabel("Pendapatan Bersih")
plt.show()

# Simpan hasil analisis diskon
df.to_csv("analisis_diskon.csv", index=False)
print("File analisis diskon berhasil disimpan sebagai: analisis_diskon.csv")

# ============================================================
# END
# ============================================================
