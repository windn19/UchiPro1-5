import itertools

n = int(input())

for pair in itertools.combinations(range(1, n + 1), 2):
    print(*pair)