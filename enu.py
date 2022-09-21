# lista = ["a", "b", "c", 4, 5, 6]
#
# for count, i in enumerate(lista, 1):
#     print("Iteracja nr: ", count, "Wartość:", i)

def test(*args, **kwargs):
    pass


def duzo(*liczby, **klucze):
    print(liczby)
    print(klucze)


# duzo()
# duzo(imie="Tomek")
# duzo(45, imie="Tomek")
# duzo(45)


def maksimum(cyfra, *liczba):
    print(cyfra)
    if len(liczba) == 0:
        return None
    else:
        liczba_max = liczba[0]
        for n in liczba[1:]:
            if n > liczba_max:
                liczba_max = n
        return liczba_max


print(maksimum(55, 100, -500, 56))
