def ganjil(a,b):
    if a < b and a%2 == 0 and b%2 == 0:
        for i in range(a+1,b,2):
            print(i, end=', ')
    elif a < b and a%2 != 0 and b%2 == 0:
        for i in range(a,b+1,2):
            print(i, end=', ')
    elif a < b and a%2 == 0 and b%2 != 0:
        for i in range(a+1,b+1,2):
            print(i, end=', ')
    elif a < b and a%2 != 0 and b%2 != 0:
        for i in range(a,b+1,2):
            print(i, end=', ')
    elif a > b and a%2 == 0 and b%2 == 0:
        for i in range(a-1,b,-2):
            print(i, end=', ')
    elif a > b and a%2 != 0 and b%2 == 0:
        for i in range(a,b-1,-2):
            print(i, end=', ')
    elif a > b and a%2 == 0 and b%2 != 0:
        for i in range(a-1,b-1,-2):
            print(i, end=', ')
    elif a > b and a%2 != 0 and b%2 != 0:
        for i in range(a,b-1,-2):
            print(i, end=', ')
    
        

a = int(input("Masukkan angka A = "))
b = int(input("Masukkan angka B = "))
ganjil(a,b)

