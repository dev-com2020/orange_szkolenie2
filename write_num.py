# outfile = open('numbers.log', 'w')
outfile = open('numbers.log', 'r')

# str_input = outfile.readline()
# value = int(str_input)
# print(value)
# print(type(value))


value = int(outfile.readline())
print(value)
print(type(value))

# num1 = int(input("Podaj liczbę:"))
# num2 = int(input("Podaj 2 liczbę:"))
# num3 = int(input("Podaj 3 liczbę:"))
#
#
# outfile.write(str(num1) + '\n')
# outfile.write(str(num2) + '\n')
# outfile.write(str(num3) + '\n')

outfile.close()

