import kl_dom

# lista = [i for i in range(10) if i % 2 == 0]
# print(lista)
#
# slownik = {1: "Azor", 2: "Reksio", 3: "Burek"}
# print({wartosc: klucz for klucz, wartosc in slownik.items()})
#
# lista1 = [1, 2, 2, 3, 4, 4, 5]
# zbior = {i for i in lista1}
# print(zbior)
#
# lista2 = ["1", "22", "33", "4"]
# liczba = [int(i) for i in lista2]
# print(liczba)

dom1 = kl_dom.Dom(basen=True, kolor_domu="zielony", ilosc_okien=5)
dom3 = kl_dom.Dom(kolor_domu="czarny", ilosc_okien=3)

# dom1.kolor_domu = "czerwony"
# dom1.ilosc_okien = 5
# dom1.basen = False
dom3.zacznij()
dom3.wstaw_okna()
dom3.maluj()


dom1.zacznij()
dom1.wstaw_okna()
dom1.maluj()

# dom2 = kl_dom.Dom()

# dom2.kolor_domu = "żółty"
# dom2.ilosc_okien = 7
# dom2.basen = True

# dom2.zacznij()
# dom2.wstaw_okna()
# dom2.maluj()
