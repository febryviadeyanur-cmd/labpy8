Nama        : Febryvia Deya Nur Havidtar Murti Aqsa

NIM         : 312510194

Kelas       : TI.25.A.2

Mata Kuliah : Pengantar Pemrograman

Pertemuan   : 13

## PRAKTIKUM 8 ##

## Penanganan Eksepsi dalam Python

Modul praktikum ini bertujuan untuk mengajarkan cara menangani kesalahan yang terjadi saat program berjalan (runtime error) agar program tidak berhenti secara tiba-tiba, membuat program lebih tangguh (robust)

## Tujuan Praktikum ##

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. Memahami konsep runtime error dan perbedaannya dengan syntax error. 

2. Menerapkan blok try-except untuk menangani kesalahan program agar tidak berhenti secara tiba-tiba. 

3. Menangani berbagai jenis eksepsi secara spesifik (seperti ValueError, ZeroDivisionError). 

4. Menggunakan klausa else dan finally untuk struktur logika yang lebih robust. 

5. Membuat dan memicu (raise) eksepsi sendiri. 

# Dasar Teori 

Dalam pemrograman, kesalahan sering terjadi saat runtime (saat program berjalan), seperti pembagian dengan nol atau mencoba mengakses indeks list yang tidak ada. Python menyediakan mekanisme standar yang disebut Exception Handling untuk menangani situasi ini.

Pendekatan Python sering disebut EAFP (Easier to Ask for Forgiveness than Permission), di mana kita mencoba menjalankan kode terlebih dahulu di dalam blok try, dan jika gagal, kita "meminta maaf" atau menanganinya di blok except2. Ini berbeda dengan pendekatan LBYL (Look Before You Leap) yang menggunakan banyak pengecekan if sebelum melakukan aksi.

## Percobaaan 1

#_Mengamati Runtime Error_

Tujuan : program menemukan kesalahan saat dijalankan

#Kode Python :

  num = int(input()) #input dari user sebagai string

  num = int(input) # string menjadi integer (angka bulat)

  print(num1 / num2) 

Jika dibagi 0 akan terjadi error = ZeroDivisionError : division by zero

#Penjelasan :

1. Buat file baru bernama percobaan1.py. 

2. Ketik kode berikut yang meminta input pengguna untuk pembagian bilangan:

Python 

  print('Silakan masukkan dua angka untuk pembagian.') 

  num1 = int(input('Masukkan angka yang akan dibagi: ')) 

  num2 = int(input('Masukkan angka pembagi: ')) 

  print('{0} dibagi {1} = {2}'.format(num1, num2, num1/num2)) 

3. Jalankan program. Masukkan angka pembagi 0

4. Analisis: Program akan berhenti mendadak dan menampilkan pesan Traceback dengan error ZeroDivisionError: division by zero

Hasilnya =

Berhasil :

<img width="1251" height="496" alt="Berhasil" src="https://github.com/user-attachments/assets/48bf5c14-3f16-477a-8ab2-d3228eef7a23" />

Error :

<img width="1133" height="576" alt="Error" src="https://github.com/user-attachments/assets/823afd51-7177-4513-a270-ad6cbb091d80" />

Kesimpulan : Program menunjukkan bahwa tanpa penanganan error, kesalahan seperti pembagian dengan nol akan menyebabkan program berhenti secara tiba-tiba (crash). Ini membantu memahami apa itu runtime error 

## Percobaan 2

#_Penanganan Error Sederhana (try-except)_

Tujuan : Mencegah program mati mendadak waktu ada error

#Kode Python :

  try:
      ...
    
      print(num1 / num2)
  
  except ZeroDivisionError:
   
      print("Tidak bisa membagi dengan nol.")

#Penjelasan :

1. Modifikasi kode percobaan1.py menjadi seperti berikut: 

Python 

    print('Silakan masukkan dua angka untuk pembagian.') 
  
    try: 
    
    num1 = int(input('Masukkan angka yang akan dibagi: ')) 
    
    num2 = int(input('Masukkan angka pembagi: ')) 
    
    print('{0} dibagi {1} = {2}'.format(num1, num2, num1/num2)) 
    
    except ZeroDivisionError: 
    
    print('Error : Tidak bisa membagi bilangan dengan nol.') 

2. Jalankan kembali dan masukkan pembagi 0. 

3. Analisis : Program tidak lagi menampilkan pesan error merah yang menakutkan, melainkan pesan sopan yang kita tentukan. Eksekusi program lompat ke blok except saat error terjadi.

Hasilnya =

Berhasil :

<img width="1132" height="513" alt="Berhasil" src="https://github.com/user-attachments/assets/2a9c67a6-2169-4d8e-9978-a4cefbcd23a4" />

Error :

<img width="1216" height="484" alt="Error" src="https://github.com/user-attachments/assets/e22d96a0-8b6f-4c11-a773-7ce3ad01da84" />

Kesimpulan : Dengan menggunakan try-except, error seperti ZeroDivisionError bisa ditangani sehingga program tetap berjalan. Ini membuktikan bahwa exception handling membuat program lebih aman dan user-friendly

## Percobaan 3

#_Menangani Berbagai Tipe Eksepsi_

Tujuan : menangani beberapa tipe error

Kode meminta input angka lalu dipakai untuk membagi 10

#Penjelasan Error :
  
  -Masukkan huruf = ValueError
  
  -Masukkan 0 = ZeroDivisionError
  
  -Error lain = Exception

#Kode Python:

  -User input huruf: "satu", "abc", dan lain-lain
  -int() tidak bisa convert huruf ke angka
  -Masuk except ValueError

#Penjelasan :

1. Buat file percobaan3.py. Kita akan menangani dua jenis error sekaligus. 

Python

    try: 
  
    val = int(input("Masukkan sebuah bilangan bulat positif: ")) 
    
    print("Anda memasukkan:", val) 
    
    hasil = 10 / val 
    
    print("10 dibagi angka tersebut adalah:", hasil) 
    
    except ValueError: 
  
    print("Input salah! Pastikan Anda memasukkan angka, bukan huruf.") 
    
    except ZeroDivisionError: 
    
    print("Input salah! Angka tidak boleh nol.") 
    
    except Exception as e: 
    
    print(f"Terjadi error yang tidak diketahui: {e}") 

2.Uji Coba: 

○ Masukkan huruf (misal: "satu") -> Akan ditangkap oleh except ValueError 

○ Masukkan angka 0 -> Akan ditangkap oleh except ZeroDivisionError

○ Masukkan angka 5 -> Program berjalan normal

Catatan: except Exception adalah penangkap umum (catch-all) untuk error yang tidak terduga, sebaiknya diletakkan di urutan terakhir

Hasilnya =

Berhasil :
<img width="1427" height="443" alt="Berhasil" src="https://github.com/user-attachments/assets/8dd03c2f-6300-42fe-b2ae-ca7ba6626e5e" />

<img width="1332" height="504" alt="Berhasil Angka" src="https://github.com/user-attachments/assets/22396798-dacd-4df6-81f3-509eb400650f" />

Error :
<img width="1251" height="501" alt="Error" src="https://github.com/user-attachments/assets/8cc46fdf-a342-4ac8-a950-7bfe21ee8e15" />

<img width="1399" height="403" alt="Error Huruf" src="https://github.com/user-attachments/assets/ad285381-b058-4c28-bf78-1b3e3a79a715" />

Kesimpulan : Program dapat menangani lebih dari satu jenis error secara spesifik, misalnya ValueError dan ZeroDivisionError. Penggunaan beberapa blok except membantu memberikan respon yang sesuai untuk setiap jenis kesalahan

## Percobaan 4

_Menggunakan Klausa else dan finally_

Tujuan : Mengenal struktur lengkap try-except

Kode Python :

  try:
   
        x = int(input("Masukkan angka: "))
    
    except ValueError:
    
        print("Itu bukan angka!")
    
    else:
    
        print("Anda memasukkan:", x)
    
    finally:
      
        print("Proses selesai.")

Penjelasan kode :

  -try = menjalankan kode yang rawan error
  
  -except = menangkap error
  
  -else = jalan hanya kalau tidak ada error
  
  -finally = selalu jalan, mau error atau tidak

Klausa else berjalan jika tidak ada eksepsi, sedangkan finally selalu berjalan (biasanya untuk bersih-bersih memori atau menutup file). 

#Penjelasan :

  1. Buat file percobaan4.py:

Python 
 
  try: 
  
  x = int(input("Masukkan angka: ")) 
  
  except ValueError: 
  
  print("Itu bukan angka!") 
  
  else: 
  
  print(f"Terima kasih, Anda memasukkan angka {x}") 
  
  #Logika lanjutan yang aman dijalankan jika input benar 
  
  finally: 
  
  print("Sesi input selesai (blok finally selalu dieksekusi).") 
  
  2. Jalankan program dengan input benar dan input salah untuk melihat beda 

Hasilnya =

Berhasil :

<img width="1212" height="441" alt="Berhasil" src="https://github.com/user-attachments/assets/4e6ded3e-fbef-458b-bd59-608282c2838c" />

Error :

<img width="1152" height="533" alt="Error" src="https://github.com/user-attachments/assets/61488f76-53b6-427c-a3d9-3b39f06242b5" />

Kesimpulan : else digunakan untuk menjalankan kode jika tidak ada error, sedangkan finally selalu dijalankan, meskipun terjadi error. Ini menegaskan struktur lengkap penanganan eksepsi dalam Python untuk logika program yang lebih terkontrol

## Percobaan 5

#_Mengakses Objek Eksepsi_

Tujuan : Menampilkan detail pesan error dari sistem

#Kode Python :

  except ValueError:
  
      print("Input harus angka.")
  
  except ZeroDivisionError:
  
      print("Angka tidak boleh nol.")
  
  except Exception as e:
  
      print("Error tidak diketahui:", e)

Penjelasan kode :

1. Masukkan huruf = ValueError

2. Masukkan 0 = ZeroDivisionError

3. Error lain = Exception

Melihat detail pesan error asli dari sistem namun tetap menanganinya menggunakan kata kunci as.

#Penjelasan :

1. Buat file percobaan5.py: 
Python 

  try: 
  
  daftar_angka = [1, 2, 3] 
  
  indeks = int(input("Masukkan indeks yang ingin diakses (0-2): ")) 
  
  print("Nilai:", daftar_angka[indeks]) 
  
  except IndexError as e: 
  
  print("Terjadi IndexError. Pesan sistem:", e) 
  
  except ValueError as e: 
  
  print("Terjadi ValueError. Pesan sistem:", e) 

2.Cobalah mengakses indeks 5. Pesan error asli list index out of range akan tersimpan dalam variabel e.

Hasilnya =

Berhasil :

<img width="1270" height="381" alt="Berhasil (1)" src="https://github.com/user-attachments/assets/f2ccf2de-8694-49ed-99d0-e5125daf26d9" />

<img width="1150" height="402" alt="Berhasil (2)" src="https://github.com/user-attachments/assets/6a52d9f5-4ac9-45b4-8da5-95209e9adebb" />

Error :

<img width="1325" height="423" alt="Error" src="https://github.com/user-attachments/assets/7ee6ce2e-458d-4ae1-8676-d4bd4313cc74" />

Kesimpulan : Penggunaan as e memungkinkan kita melihat pesan asli dari error. Ini berguna untuk debugging dan memberi informasi lebih detail kepada pengguna


## Percobaan 6

#_Memicu Eksepsi Sendiri (raise)_

Tujuan : program belajar membuat error secara manual

#Kode Python : 

  def cek_level(level):
     
      if level < 1:
      
          raise ValueError("Level tidak valid! Harus minimal 1.")

raise digunakan jika kamu ingin:

1. memblok input tidak valid

2. memaksa program menghentikan proses tertentu

3. memastikan nilai memenuhi syarat

4. Ini bentuk validasi manual

#Penjelasan :
 
  1. Buat file percobaan6.py: 

Python 
  
    def cek_level(level): 
    
    if level < 1: 
    
    raise ValueError("Level tidak valid! Harus minimal 1.") 
    
    print(f"Level {level} diterima.") 
    
    try: 
    
    lvl = int(input("Masukkan level karakter: ")) 
    
    cek_level(lvl) 
    
    except ValueError as e: 
 
    print("Peringatan:", e) 
  
  2. Masukkan angka -5. Fungsi akan "melempar" error yang kemudian "ditangkap" oleh blok except

Hasilnya =

Berhasil :

<img width="1274" height="390" alt="Berhasil (1)" src="https://github.com/user-attachments/assets/992c7f28-da91-447f-8ef6-618ae7acb2f1" />

<img width="1173" height="435" alt="Berhasil (2)" src="https://github.com/user-attachments/assets/49e39339-d772-4b0b-8218-296c21286b34" />

Error :

<img width="1310" height="404" alt="Error" src="https://github.com/user-attachments/assets/61631a2c-5067-47b0-8600-1e567395e54f" />

Kesimpulan : Dengan raise, programmer dapat membuat error sendiri untuk memastikan bahwa input atau kondisi tertentu memenuhi syarat. Ini berguna untuk validasi dan keamanan logika program.


.


.

## TUGAS MANDIRI ##

## Latihan 1 = KALKULATOR AMAN

Tujuan : Membuat program kalkulator sederhana yang meminta dua angka dan satu operator, lalu menggunakan try-except dan raise untuk menangani semua kemungkinan error

#Program ini memiliki fitur:

1. Menangani input yang bukan angka dengan ValueError

2. Menangani pembagian dengan nol dengan ZeroDivisionError

3. Validasi operator dengan raise Exception untuk operator tidak valid

4. Menggunakan finally untuk pesan penutup

#Cara kerja:

1. Program meminta 2 angka dan 1 operator

2. Jika input bukan angka → error tertangani

3. Jika operator selain +, -, *, / → error kustom muncul

4. Jika membagi dengan 0 → error tertangani

#Kode Python :

  try:
    
    angka1 = float(input("Masukkan angka pertama: "))
    
    angka2 = float(input("Masukkan angka kedua: "))

#Penjelasan kode :

1. ValueError: Ditangkap ketika float(num1) atau float(num2) gagal karena pengguna memasukkan teks (misal: "sepuluh").

2. ZeroDivisionError: Ditangkap jika operator adalah '/' dan nilai b (angka pembagi) adalah 0.

3. raise Exception: Digunakan untuk kasus di mana logika program (operator) tidak terpenuhi. Ini menciptakan error kustom yang kemudian ditangkap oleh except Exception as e

Hasilnya =

-Pertambahan :

<img width="1288" height="535" alt="Pertambahan" src="https://github.com/user-attachments/assets/01838f37-8474-4da0-a6e9-8b14e1642aab" />

-Pengurangan :

<img width="1287" height="442" alt="Pengurangan" src="https://github.com/user-attachments/assets/5e577c89-212c-4ad7-9243-cd6363188ac4" />

-Pembagian :

<img width="1441" height="480" alt="Pembagian" src="https://github.com/user-attachments/assets/d82c4e7b-9c73-4548-ae83-c072217ae6d1" />

-Perkalian :

<img width="1300" height="473" alt="Perkalian" src="https://github.com/user-attachments/assets/85f6e08e-69a6-4564-8c13-b21fea6567f4" />

Kesimpulan : menunjukkan bahwa penggunaan try-except membuat program lebih aman, tidak mudah crash, dan dapat memberikan pesan kesalahan yang jelas kepada pengguna. Selain itu, teknik raise membantu memvalidasi input sehingga program dapat mengontrol secara logika

## Latihan 2 = Validasi Daftar Nilai  ##

Tujuan : 

1. Looping satu per satu nilai

2. Ubah ke int()

3. Kalau berhasil masuk hitungan

4. Kalau gagal (huruf) lewati dengan except

5. Hitung rata-rata hanya dari nilai yang valid

#Dengan menggunakan try-except di dalam perulangan:

-Data yang valid (angka) berhasil dijumlahkan

-Data yang tidak valid (huruf seperti 'A' dan 'B') dilewati tanpa menghentikan program

-Hanya nilai yang valid yang dihitung rata-ratanya

#Kode Python :

nilai = [80, 90, 'A', 70, 100, 'B']

- 80, 90, 70, 100 → data valid (angka)

- 'A', 'B' → data tidak valid (string)

Python bakal error karena 'A' dan 'B' tidak bisa diubah menjadi angka

Hasilnya :

<img width="1464" height="724" alt="Hasil py" src="https://github.com/user-attachments/assets/db88a754-c606-4a32-a8f2-7ebe4868da32" />

Kesimpulan : menunjukkan bahwa exception handling sangat berguna untuk membersihkan data, yaitu memisahkan data yang valid dan tidak valid tanpa membuat program berhenti

Commit dan push :

<img width="1241" height="765" alt="Screenshot 2025-12-11 202811" src="https://github.com/user-attachments/assets/17de883f-020e-49df-b894-ded541c1e2aa" />
