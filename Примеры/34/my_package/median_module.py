PRECISION = 3


def median(iterable, precision=PRECISION):
   sorted_iterable = sorted(iterable)
   length = len(iterable)
   if length % 2 != 0:
       return sorted_iterable[length // 2]
   result = sum((sorted_iterable[length // 2 - 1: length // 2 + 1])) / 2
   return round(result, precision)

