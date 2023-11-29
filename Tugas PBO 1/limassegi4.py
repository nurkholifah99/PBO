print("Menghitung Volume Limas Segi Empat")

# Input
Alas_Segitiga = float(input("masukkan Alas Segitiga:"))
Tinggi_Segitiga = float(input("masukkan Tinggi Segitiga:"))
Tinggi_Limas = float(input("masukkan Tinggi Limas:"))

# Rumus
Luas_Segitiga= (1/2)*Alas_Segitiga*Tinggi_Segitiga
Volume = (1/3)*Luas_Segitiga*Tinggi_Limas

# Output
print(f"Volume prisma segitiga adalah: {Volume}")