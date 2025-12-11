    #TUGAS MANDIRI
    #KALKULATOR AMAN

print ("KALKULATOR AMAN")

try:
    # Input angka pertama
    angka1 = float(input("Masukkan angka pertama: "))

    # Input angka kedua
    angka2 = float(input("Masukkan angka kedua: "))

    # Input operator
    operator = input("Masukkan operator (+, -, *, /): ")

    # Validasi operator
    if operator not in ['+', '-', '*', '/']:
        raise Exception(f"Operator '{operator}' tidak valid! Gunakan +, -, *, atau /")

    # Proses perhitungan
    if operator == '+':
        hasil = angka1 + angka2
    elif operator == '-':
        hasil = angka1 - angka2
    elif operator == '*':
        hasil = angka1 * angka2
    elif operator == '/':
        # Cek pembagian dengan nol
        if angka2 == 0:
            raise ZeroDivisionError("Tidak bisa membagi dengan nol!")
        hasil = angka1 / angka2

    # Tampilkan hasil
    print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")

except ValueError:
    print("Error: Input harus berupa angka!")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Terima kasih telah menggunakan kalkulator!")