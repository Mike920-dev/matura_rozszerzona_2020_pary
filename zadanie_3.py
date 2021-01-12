def para(min_para, sprawdzana_para):
    liczba_min_para = int(min_para[0])
    slowo_min_para = min_para[1].strip()
    liczba_sprawdzana_para = int(sprawdzana_para[0])
    slowo_sprawdzana_para = sprawdzana_para[1].strip()

    if liczba_sprawdzana_para != len(slowo_sprawdzana_para):
        return False
    if liczba_sprawdzana_para < liczba_min_para:
        return True
    if (liczba_sprawdzana_para == liczba_min_para and slowo_sprawdzana_para < slowo_min_para):
        return True
    return False

with open("pary.txt", "r", encoding="UTF-8") as plik:
    pary = []

    for line in plik:
        pary.append(line.split())

# print(pary)
min_para = pary[0]

for i in range(100):
    sprawdzana_para_teraz = pary[i]
    if para(min_para, sprawdzana_para_teraz):
        min_para = sprawdzana_para_teraz

print(f'{min_para[0]} {min_para[1]}')

with open("wyniki4.txt", "a", encoding="UTF-8") as plik:
    plik.write(f'c) \n')
    plik.write(f'{min_para[0]} {min_para[1]}')
    
