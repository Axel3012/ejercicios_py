from sumas import sumatorio
from functools import reduce

print(
    reduce(lambda a, b: a + b, range(100 + 1)),
    sumatorio(100)
)

print(
    reduce(lambda a, b: a + 2 * b + 1, range(15 + 1), 0),
    sumatorio(15, lambda x: 2 * x + 1)
)