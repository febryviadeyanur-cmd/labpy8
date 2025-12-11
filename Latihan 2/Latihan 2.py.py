    #TUGAS MANDIRI
    #PROGRAM VALIDASI DAFTAR NILAI

print("PROGRAM VALIDASI DAFTAR NILAI")

# Daftar nilai mahasiswa
nilai = [80, 90, 'A', 70, 100, 'B']

print(f"Daftar nilai: {nilai}")
print("Memproses nilai")

# Menyimpan hasil
total_nilai = 0
jumlah_valid = 0

# Iterasi (looping) setiap nilai dalam list
for item in nilai:
    try:
        # Konversi ke angka dan tambahkan ke total
        angka = float(item)
        total_nilai += angka
        jumlah_valid += 1
        print(f"Nilai {item} berhasil diproses")
    except (ValueError, TypeError):
        # Jika tidak bisa dikonversi, melewati (skip) data
        print(f"Data '{item}' bukan angka, dilewati")

# Hitung dan tampilkan rata-rata
print("HASIL PERHITUNGAN")

if jumlah_valid > 0:
    rata_rata = total_nilai / jumlah_valid
    print(f"Total nilai valid: {total_nilai}")
    print(f"Jumlah data valid: {jumlah_valid}")
    print(f"Rata-rata nilai: {rata_rata:.2f}")
else:
    print("Tidak ada data valid untuk dihitung!")