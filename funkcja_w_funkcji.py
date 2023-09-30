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
