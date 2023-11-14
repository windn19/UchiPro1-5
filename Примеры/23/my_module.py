PRECISION = 3


def average(iterable, precision=PRECISION):
    return round(sum(iterable) / len(iterable), precision)
