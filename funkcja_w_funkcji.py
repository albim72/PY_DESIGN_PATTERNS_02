#przykład1
#funkcje wyższego rzędu -> funkcje które posiadają minimum jeden argument reprezentujący funckję

def witaj(imie):
    return f'dziękujęmy za założenie konta: {imie}'

def egzamin(imie,punkty,zaliczono):
    return f'osoba egzaminowana: {imie}, liczba punktów: {punkty}, wynik egzaminy -> zdany? {zaliczono}'

def obliczenie(x,y,z):
    return (x+y)**z

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(egzamin,"Olga",56,True))
print(osoba(obliczenie,5,2,3))

#przykład 2
liczba = [3,6,9,19,78,1134,-67,0,-9,34,6,-11,888,-33,-342,222,10]

parzyste = list(filter(lambda x:x%2==0,liczba))
print(parzyste)

cube = list(map(lambda x:x**3,liczba))
print(cube)

#przykład 3 - funkcje wewnętrzne

def rejestracja(oplata):
    def lista_zawodnikow(nrlisty):
        return f"jesteś na liście zawodników nr {nrlisty}"

    def brak():
        return "brak wpłaty, uzupełnij w ciągu 3 dni"

    def error():
        return "błąd księgowania wpłaty![1- wpłata, 0-brak, inna wartość - błąd!]"

    if oplata == 1:
        return lista_zawodnikow(453)
    elif oplata == 0:
        return brak()
    else:
        return error()

print(rejestracja(1))
print(rejestracja(44))
print(rejestracja(0))

