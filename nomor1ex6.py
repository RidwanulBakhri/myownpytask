def Pythagoras(a, b, c):
    numbers = a**2 + b**2
    pythagoras = numbers == c**2
    print(pythagoras)

# Untuk input angka bisa kita lakukan dengan menggunakan int(input("Masukkan angka : ")) setelah code di-run atau memanggil fungsi dan mengisi langsung data di dalamnya sebelum code di-run
# seperti di bawah ini
Pythagoras(int(input("Masukkan angka : ")), int(input("Masukkan angka : ")), int(input("Masukkan angka : ")))
# atau seperti ini
Pythagoras(3,4,5)