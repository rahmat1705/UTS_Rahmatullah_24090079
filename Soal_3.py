# Program untuk menghitung total harga belanjaan

# memasukkan jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Inisialisasi total harga
total_harga = 0

# memasukkan harga setiap barang
for i in range(jumlah_barang):
    harga_barang = float(input(f"Masukkan harga barang ke-{i + 1}: "))
    total_harga += harga_barang  # Menambahkan harga barang ke total

# Menampilkan total harga belanjaan
print(f"\nTotal harga belanjaan adalah: {total_harga}")