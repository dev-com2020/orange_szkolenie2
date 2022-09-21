import random


class Coin():
    def __init__(self):
        self.__sideup = 'orzeł'

    def rzut(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'orzeł'
        else:
            self.__sideup = 'reszka'

    def get_sideup(self):
        return self.__sideup


moneta = Coin()
moneta.rzut()
# moneta.__sideup = 5454545454545
print("Wynik rzutu monetą:", moneta.get_sideup())




