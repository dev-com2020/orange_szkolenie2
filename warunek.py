wiek = int(input("Ile masz lat?"))

if wiek < 18:
    print("Nie możesz wejść na stronę.")
elif wiek == 18:
    print("Gratulacje, masz 18 lat!")
elif 19 < wiek < 100:
    print("Masz 19 do 100 lat")
    plec = input("Podaj płeć(k/m):")
    if plec == 'k':
        print("kobieta")
    else:
        print("mężczyzna")
else:
    print("masz powyżej 100 lat!")




