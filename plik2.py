file = open('plik.txt', 'r')

linia1 = file.readline()
linia2 = file.readline()

zbior = linia2, linia1
imie1, imie2 = zbior
imie1 = imie1.rstrip('\n')
imie2 = imie2.rstrip('\n')

print(type(zbior))
print(zbior)
print(imie1)
print(imie2)
# zawartosc = file.read()
# print(type(zawartosc))
# print(zawartosc)
file.close()

