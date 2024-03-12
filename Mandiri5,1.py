def perkalian(a,b):
    i = 0
    x = 0
    print(a," x ",b,"= ", end='')
    while i < a:
        i = i + 1
        x = x + b
        if i < a:
            print(b,"+ ", end='')
        else:
            print(b, "= ", end='')
    print(x)

a = int(input("Masukkan angka pengkali = "))
b = int(input("Masukkan angka dikali = "))
perkalian(a,b)