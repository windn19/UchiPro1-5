from . import constants


# from .constants import PRECISION

def avg(iterable, precision=constants.PRECISION):
    return round(sum(iterable) / len(iterable), precision)
