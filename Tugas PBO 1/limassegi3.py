print("Menghitung Volume Limas Segi Tiga")

# Input
Panjang_Sisi_Alas = float(input("masukkan Panjang Sisi Alas:"))
Tinggi_Segitiga = float(input("masukkan Tinggi Segitiga:"))
Tinggi_Limas = float(input("masukkan Tinggi Limas:"))

# Rumus
Luas_Alas = (1/2)*Panjang_Sisi_Alas*Tinggi_Segitiga
Volume = (1/3)*Luas_Alas*Tinggi_Limas

# Output
print(f"Volume Limas Segi Tigas adalah: {Volume}")