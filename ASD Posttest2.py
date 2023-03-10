import os

print('''
|       Remanda Dheva        |
|        2209116034          |
|        SI A 2022           |
''')

def fibonacci(k, d, j):
    fib1 = 0
    fib2 = 1
    fibonacci = fib1 + fib2
    while (fibonacci < j):
        fib1 = fib2
        fib2 = fibonacci
        fibonacci = fib1 + fib2
    offset = -1

    while (fibonacci > 1):
        i = min(offset + fib1, j-1)
        if (k[i] < d):
            fibonacci = fib2
            fib2 = fib1
            fib1 = fibonacci - fib2
            offset = i
        elif (k[i] > d):
            fibonacci = fib1
            fib2 = fib2 - fib1
            fib1 = fibonacci - fib2
        else:
            return i
    if (fib2 and k[j-1] == d):
        return j-1
    return -1

def search():
    while True:
        cari = input("Masukan Nama Yang Ingin Anda Cari : ")
        os.system("cls")
        print("="*25, "Mencari Nama", cari, "="*25)

        for v in range(len(Data)):
            if type(Data[v]) == list:
                column = fibonacci(Data[v], cari, len(Data[v]))
                print(cari, "Berada Di Index Ke : ", v, "Pada Kolom", column)
                return
            else:
                if Data[v] == cari:
                    print(cari, "Berada Di Index Ke : ",v)
                    return
                
def start():
    os.system("cls")
    while True:
        print("~"*63)
        print('''
|                       SELAMAT DATANG                        |
|               APAKAH ADA YANG BISA DIBANTU?                 |
|                    1. MENCARI DATA NAMA                     |
|                    2. KELUAR                                |
        ''')
        print("~"*63)
        try:
            menu = int(input("Silahkan Pilih Menu: "))
            if menu == 1:
                print("="*71)
                print(f"Data Nama Yang Tersedia: {Data}")
                print("="*71)
                search()
            elif menu == 2:
                print("="*20, "SAMPAI JUMPA LAGI", "="*20)
                break
        except:
            print("Input Tidak Valid")

Data = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

start()