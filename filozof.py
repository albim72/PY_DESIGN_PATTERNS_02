odp = input("Czy Ziemia jest płaska? Chcesz znać odpowiedź? (t/n) ")

if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self,*args):
    return "Tak! Ziemia jest płaska!"

def new_odpowiedz(self,*args):
    return "Nie! Ziemia jest elipsoidą!"

def brak(self):
    return "brak odpowiedzi..."

class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,attrs):
        if required:
            if attrs.get('n'):
                cls.odpowiedz = new_odpowiedz
            else:
                cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

class Kopernik(metaclass=SednoOdpowiedzi):
    n = True

class Enstein(metaclass=SednoOdpowiedzi):
    n = True

fil1 = Arystoteles()
print(f'Filozof {fil1.__class__.__name__} twierdzi: {fil1.odpowiedz()}')

fil2 = Platon()
print(f'Filozof {fil2.__class__.__name__} twierdzi: {fil2.odpowiedz()}')

fil3 = SwTomasz()
print(f'Filozof {fil3.__class__.__name__} twierdzi: {fil3.odpowiedz()}')

fil4 = Kopernik()
print(f'Filozof {fil4.__class__.__name__} twierdzi: {fil4.odpowiedz()}')

fil5 = Enstein()
print(f'Filozof {fil5.__class__.__name__} twierdzi: {fil5.odpowiedz()}')
