from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x

    def msg(self,m):
        return f'kod numer: {m}'

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*9


class Regular(Prototyp):

    def __init__(self, x ,y):
        super().__init__(x)
        self.y = y

    def policz(self):
        return 2001

    def policz_x(self):
        return super().policz_x() + self.y*2


re = Regular(3,6)
print(f'funkcja policz() zwraca wartość {re.policz()}')
print(f'funkcja policz_x() zwraca wartość {re.policz_x()}')
