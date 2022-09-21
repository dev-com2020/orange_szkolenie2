lista = [i for i in range(10) if i % 2 == 0]
print(lista)

slownik = {1: "Azor", 2: "Reksio", 3: "Burek"}
print({wartosc: klucz for klucz, wartosc in slownik.items()})

lista1 = [1, 2, 2, 3, 4, 4, 5]
zbior = {i for i in lista1}
print(zbior)

lista2 = ["1", "22", "33", "4"]
liczba = [int(i) for i in lista2]
print(liczba)
