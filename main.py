import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === 1. Baca data ===
data = pd.read_csv('Nilai_siswa.csv', sep=';')

# === 2. Tampilkan informasi dasar ===
print("=== Data Awal ===")
print(data.head(), "\n")

print("=== Statistik Deskriptif ===")
print(data.describe(), "\n")

# === 3. Statistik Nilai ===
mean_nilai = data['Nilai'].mean()
median_nilai = data['Nilai'].median()
modus_nilai = data['Nilai'].mode()[0]

print("Rata-rata :", mean_nilai)
print("Median    :", median_nilai)
print("Modus     :", modus_nilai, "\n")

# === 4. Nilai maksimum dan minimum per mata pelajaran ===
print("=== Nilai Maksimum & Minimum per Mata Pelajaran ===")
print(data.groupby('Matpel')['Nilai'].agg(['max', 'min']), "\n")

# === 5. Visualisasi Rata-Rata Nilai per Mata Pelajaran ===
plt.figure(figsize=(8, 5))
rata_per_mapel = data.groupby('Matpel')['Nilai'].mean()
rata_per_mapel.plot(kind='bar', color='lightcoral', edgecolor='black')

plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === 6. Boxplot Sebaran Nilai ===
plt.figure(figsize=(8, 5))
sns.boxplot(x='Matpel', y='Nilai', data=data, palette='pastel')

# === Sebaran Nilai per Mata Pelajaran (BOXPLOT seperti gambar) ===
plt.figure(figsize=(12, 6))

sns.boxplot(
    data=data,
    x='Matpel',
    y='Nilai',
    palette='pastel'  
)

plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()