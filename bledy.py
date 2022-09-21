def mnozenie(a, b):
    try:
        return int(a) * int(b)
    except (ValueError, TypeError):
        return 'Błąd nr 323: nie udało się!'


def mnozenie2(a, b):
    try:
        return int(a) * int(b)
    except Exception as e:
        return 'błąd programu: nie udało się!', e


def mnozenie3(a, b):
    try:
        wynik = int(a) * int(b)
    except ValueError:
        return 'błąd programu nr 1111: nie udało się!'
    except TypeError:
        return 'błąd programu nr 4311: nie udało się!'
    else:
        return wynik
    finally:
        print("Zawartość zmiennych a,b:", a, b)


def mnozenie4(a, b):
    return a * b



try:
    print(mnozenie4("4", "4"))
except Exception as e:
    print(e.__class__, e)




# print(mnozenie(None, 43))
# print(mnozenie("4", 'a'))
# print(mnozenie(4, 43))

# print(mnozenie2(None, 43))
# print(mnozenie2("4", 'a'))
# print(mnozenie2(4, 43))

# print(mnozenie3(None, 43))
# print(mnozenie3("4", 'a'))
# print(mnozenie3(4, 43))
