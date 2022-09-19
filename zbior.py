krotka = (1, 2, 3, 4, 5, 6)
krotka2 = (1, 2, 4, 5, 7, 3)

krotka_suma = krotka + krotka2

zbior2 = {1, 2, 3, 8, 9}
zbior = set(krotka_suma)
print(zbior2)
print(zbior)
print(zbior.difference(zbior2))
print(zbior2.difference(zbior))
print(zbior2 - zbior)
print(zbior2.intersection(zbior))
print(zbior.intersection(zbior2))
print(zbior & zbior2)


