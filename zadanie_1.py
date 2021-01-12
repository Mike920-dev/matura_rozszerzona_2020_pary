def czy_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    return False

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

for liczba in liczby:
    for i in range(3, 100 + 1):
        if czy_parzysta(liczba):
            if czy_pierwsza(i) and czy_pierwsza(liczba - i):
                print(liczba, ' ', i, ' ', liczba - i)
                break


with open("wyniki4.txt", "w", encoding="UTF-8") as plik:
    plik.write(f'a) ')
    for i in range(3, 100 + 1):
        if czy_parzysta(liczba):
            if czy_pierwsza(i) and czy_pierwsza(liczba - i):
                plik.write(f'{liczba} {i} {liczba - i}')
                break
    plik.write(f'\n')
