# lambda parametr/y : wyrażenie/a

# def test():
#     global a
#     a = 666
#
# test()
#
# zmienna = lambda _: _ + 1
# zmienna2 = lambda x, y: x + 1 - y
#
# a = int(input("Podaj cyfrę:"))
# print(zmienna(a))
#
# ttt = int(input("Podaj 2 cyfrę:"))
# print(zmienna2(a, ttt))


# x = int(input("podaj cyfrę: "))
# print((lambda x: x + 1)(x))

lista = [1,
         3, 5,
         7, 9]

print(f"Nasza lista {lista}")
print(f"Przykład zastosowania map: {list(map(lambda _:_ * 2,lista))}")
print(f"Przykład zastosowania map: {list(filter(lambda _:_ > 5,lista))}")


wiek = lambda x: "dziecko" if x < 10 else ("Nastolatek" if x < 18 else "Dorosły")
print(wiek(24))