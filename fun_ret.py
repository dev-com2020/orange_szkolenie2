import test

PI = (3.14,)
PI2 = 3.14

def ksero(tekst: str, ile: int):
    return (tekst + " ") * ile


# print(ksero("Witaj", 5))
# wynik = ksero("Witaj ponownie", 6)
# pytanie = input("Podaj wyraz:")
# ile_razy = int(input("Podaj ile razy:"))
# print(ksero(pytanie, ile_razy))
# lista = [wynik]
# print(lista)

# test.load_workbook()


a = 5
b = 9


def mam_global():
    global a, b
    a = 1
    b = 2
    return a + b


def nie_mam_global():
    a = 100
    c = 3
    return a + c


print(mam_global())
print(nie_mam_global())
print(a)
