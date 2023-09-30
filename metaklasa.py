class MojaMeta(type):
    def __new__(cls,clsname,bases,attrs):
        print('**********************************************')
        print(f'nazwa klasy: {clsname}')
        print(f'dziedziczone klasy: {bases}')
        print(f'zbiór atrybutów: {attrs}')
        return type.__new__(cls,clsname,bases,attrs)


class S:
    pass

class Specjalna(S,metaclass=MojaMeta):
    def info(self):
        return 123

class B(Specjalna):
    pass

class F:
    pass

class Multi(B,F):
    pass
