# skala = None
# liczba1 = int(input("Podaj pierwszą liczbę:"))
# liczba2 = float(input("Podaj drugą liczbę:"))
# wynik = liczba1 + liczba2
# wynik2 = liczba1 * liczba2
# print("Wynik dodawania=", wynik)
# print("Wynik mnożenia=", list([wynik2, wynik]))

# krotka = (1, 2, 3, 4)
# nowa_l = list(krotka)
# nowa_l.append(5)
# print(nowa_l)
# krotka = tuple(nowa_l)
# print(krotka)

slownik = {"jeden": 1,
           "dwa": [1, 2],
           3: "trzeci",
           4: {5: "pięć"}
           }

print(slownik.keys())
print(slownik.values())
slownik[3] = "nowa_wart"
slownik[6] = "Tomek"
print(slownik.items())
# print(slownik.get(4))
drugi = slownik[4]
print("dwa" in slownik)
print("pięć" in drugi.values())