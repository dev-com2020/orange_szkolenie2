print("Hej Python!")
suma = 2
temp_cels = 15.5
imie = "Tomek"
# print(type(suma))
# print(type(imie))
# print(type(temp_cels))
# print(suma * temp_cels + 55 / 4.2 - 41)

prawda = True
falsz = False

# print(suma > temp_cels)
# print(suma >= temp_cels)
# print(suma >= temp_cels)
# print(suma < temp_cels)
# print(suma == temp_cels)
# print(suma != temp_cels)

# print(suma and temp_cels)
# print(falsz and prawda)
#
# print(suma or temp_cels)
# print(prawda or falsz)
#
# print(not prawda)
# print(not not prawda)

oceny = [1, 2, 3, 4, 5]
print(oceny)
print(oceny[2:])
print(oceny[-3:-1])
print(oceny[-3:])
print(oceny[:-3])
oceny.append(6)
oceny.insert(3, "Tomek")
oceny[0] = 22
oceny.pop(-1)
oceny.remove("Tomek")
# print(oceny)

krotka = (1, 2, 3, 4, 5, 6)
krotka2 = (1, 2, 3, 4, 5, 6)
print(krotka[2:])
# print(krotka.count(5))
# oceny.extend(krotka)
# wyniki2 = oceny + list(krotka)
# wyniki = krotka2 + krotka
# oceny.sort()
# print(wyniki)
# print(wyniki2)
wyniki3 = [oceny, krotka]
print(wyniki3[0][0])
wyniki3.clear()
