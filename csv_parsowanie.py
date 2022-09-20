import csv

lista = []

with open('cities.csv', 'r', encoding='utf-8') as file:
    # reader = csv.reader(file, delimiter=',')
    reader = csv.DictReader(file)
    # print(reader.fieldnames)
    for row in reader:
        lista.append(int(row[' "LonD"']))

print(lista)

with open('wyniki.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(lista)