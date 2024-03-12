def cariips(matkul):
    sks = 3
    bobot = 0
    totalbobot = 0
    totalsks = 0
    i = 0
    while i < matkul:
        i = i + 1
        sksmatkul = (input(f"Mata Kuliah {i}:"))
        if sksmatkul == 'A':
            bobot = 4
        elif sksmatkul == 'B':
            bobot = 3
        elif sksmatkul == 'C':
            bobot = 2
        elif sksmatkul == 'D':
            bobot = 1

        totalbobot = totalbobot + bobot*sks
        totalsks = matkul*sks
    ips = totalbobot/totalsks
    print(round(ips,2))
    
        

matkul = int(input("Berapa Jumlah MataKuluah = "))
cariips(matkul)

