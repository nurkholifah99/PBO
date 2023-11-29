print("Menghitung Luas dan Volume Prisma Segi Tiga")

# Input
Tinggi_Prisma = float(input("masukkan Tinggi_Prisma:"))
Panjang_Alas = float(input("masukkan Panjang_Alas:"))
Tinggi_Segitiga = float(input("masukkan Tinggi_Segitiga:"))

# Rumus
Luas_Permukaan = (2*Panjang_Alas) + (Panjang_Alas*Tinggi_Segitiga) + (3*Panjang_Alas*Tinggi_Segitiga)
Volume = (1/2)*Panjang_Alas*Tinggi_Segitiga*Tinggi_Prisma

# Output
print(f"Luas permukaan prisma segitiga adalah: {Luas_Permukaan}")
print(f"Volume prisma segitiga adalah: {Volume}")