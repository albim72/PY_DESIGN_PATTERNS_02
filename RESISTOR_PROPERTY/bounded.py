from resistor import Resistor

class BoundedResistance(Resistor):
    stohms = 4E2
    nazwa = "czerwony"

    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self,ohms):
        if ohms <= 0:
            raise ValueError("Wartość oporności musi być większa od 0!")
        self._ohms = ohms

    @property
    def doubleohms(self):
        return 2*self.stohms

    @property
    def koloropornika(self):
        return self.nazwa

    @koloropornika.setter
    def koloropornika(self,nowykolor):
        self.nazwa = nowykolor
