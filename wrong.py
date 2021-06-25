import random


class Cars:
    def __init__(self, m, p, n):
        self.model = m
        self.price = p
        self.num = n


classList = []
for i in range(5):
    classList.append(Cars("R8", 100000, random.randint(0, 10)))

print(classList[1].num)

print(type(classList[0]))
