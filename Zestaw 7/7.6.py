import itertools
import random


it = itertools.cycle([0, 1])

for _ in range(10):
    print(next(it), end=" ")


it = (random.choice(("N", "E", "S", "W")) for _ in iter(int, 1))

print()
for _ in range(10):
    print(next(it), end=" ")

it = itertools.cycle(range(7))

print()
for _ in range(10):
    print(next(it), end=" ")

print()