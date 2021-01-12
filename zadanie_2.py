def ciag(slowo):
    obecna_litera = slowo[0]
    dlugosc_ciagu = 1
    ile_razy_wystapila_litera = 1
    wynik = (dlugosc_ciagu * obecna_litera, dlugosc_ciagu)

    for i in range(1, len(slowo)):
        if obecna_litera == slowo[i]:
            ile_razy_wystapila_litera += 1
        else:
            obecna_litera = slowo[i]
            ile_razy_wystapila_litera = 1
        if ile_razy_wystapila_litera  > dlugosc_ciagu:
            dlugosc_ciagu = ile_razy_wystapila_litera
            wynik = (dlugosc_ciagu * obecna_litera, dlugosc_ciagu)

    return wynik


with open("pary.txt", "r", encoding="UTF-8") as plik:
    pary = []

    for line in plik:
        pary.append(line.split())

# print(pary)

liczby = []
slowa = []

for liczba, slowo in pary:
    liczby.append(int(liczba))
    slowa.append(slowo)

# print(liczby)
# print(slowa)

for slowo in slowa:
    wynik = ciag(slowo)
    print(f'{wynik[0]} {wynik[1]}')


with open("wyniki4.txt", "a", encoding="UTF-8") as plik:
    plik.write(f'b) ')
    for slowo in slowa:
        wynik = ciag(slowo)
        plik.write(f'{wynik[0]} {wynik[1]} \n')
    plik.write(f'\n')
