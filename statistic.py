def Sum(a,b,c,d,e,f,g,h):
    data = [a,b,c,d,e,f,g,h]
    jumlah = sum(data)
    print(f"\nTotal      : {jumlah}")

def Average(a,b,c,d,e,f,g,h):
    data = [a,b,c,d,e,f,g,h]
    rata_rata = sum(data)/len(data)
    jumlah = sum(data)
    print(f'Average    : {rata_rata}')
    
def Maximum(a,b,c,d,e,f,g,h):
    data = [a,b,c,d,e,f,g,h]
    maksimum = max(data)
    print(f'Maks       : {maksimum}')
    
def Minimum(a,b,c,d,e,f,g,h):
    data = [a,b,c,d,e,f,g,h]
    minimum = min(data)
    print(f'Min        : {minimum}')
    
a = int(input("Masukkan Angka : "))
b = int(input("Masukkan Angka : "))
c = int(input("Masukkan Angka : "))
d = int(input("Masukkan Angka : "))
e = int(input("Masukkan Angka : "))
f = int(input("Masukkan Angka : "))
g = int(input("Masukkan Angka : "))
h = int(input("Masukkan Angka : "))
Sum(a,b,c,d,e,f,g,h)
Average(a,b,c,d,e,f,g,h)
Maximum(a,b,c,d,e,f,g,h)
Minimum(a,b,c,d,e,f,g,h)
