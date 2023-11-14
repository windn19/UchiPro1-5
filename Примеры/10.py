result = filter(lambda x: x % 2, map(lambda x: len(x), ['first', 'second', 'third']))
print(*result)