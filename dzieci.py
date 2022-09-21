from abc import abstractmethod, ABC


class Ptak(ABC):

    def __init__(self, gatunek: str, predkosc: int):
        self.gatunek = gatunek
        self.predkosc = predkosc

    def lataj(self):
        print("Tu", self.gatunek, "ja latam i osiągnę prędkość!", self.predkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, predkosc=0)

    def lataj(self):
        print("Tu", self.gatunek, 'ja nie latam :(')

    def wydajOdglos(self):
        print('kokoko')


class Orzel(Ptak):
    def poluj(self):
        print("Tu", self.gatunek, "rozpoczynam polowanie!")

    def wydajOdglos(self):
        print('piiii')


k = Kura("Stefan")
k.lataj()
k.wydajOdglos()
o = Orzel("Mietek", 100)
o.lataj()
o.poluj()
o.wydajOdglos()
