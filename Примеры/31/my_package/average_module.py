PRECISION = 3


def avg(iterable, precision=PRECISION):
   return round(sum(iterable) / len(iterable), precision)

