import random

k6 = [1, 2, 3, 4, 5, 6]
print("wynik rzutu:", random.choice(k6))

wynik = random.randint(1, 6)  # 1-6
wynik2 = random.randrange(1, 6)  # 1-5
print(random.random() * 100)
print(wynik)
