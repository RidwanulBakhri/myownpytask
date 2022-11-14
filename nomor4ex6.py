def starFormation(n):
    for x in range(1, n+1, 1):
        print("*"*x)
    for x in range(n-1, 0, -1):
        print("*"*x)
starFormation(int(input("Masukkan angka : ")))