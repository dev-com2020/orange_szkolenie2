lista = ["a", "b", "c", 4, 5, 6]

for count, i in enumerate(lista, 1):
    print("Iteracja nr: ", count, "Wartość:", i)


def duzo(*liczby, **klucze):
    print(liczby)
    print(klucze)


duzo()
duzo(imie="Tomek")
duzo(45, imie="Tomek")
duzo(45)




