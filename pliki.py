# plik = open(r'D:\dokumenty\test\nowy\plik.txt', 'r''w''a')
wybor = input("Podaj nazwę pliku do otwarcia:")
plik = open(wybor, 'a')


name = "Jan Kowalski"
name2 = "Janina Kowalska"

zbior = [name, name2]
print(zbior)

# plik.write(str(zbior))

for i in zbior:
    plik.write(i)
    plik.write("\n")

plik.close()