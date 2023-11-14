PRECISION = 3


def average(iterable, precision=PRECISION):
    return round(sum(iterable) / len(iterable), precision)


# average([1, 2, 3], precision=2)

if __name__ == '__main__':
    average([1, 2, 3], precision=2)
