from functools import lru_cache
from simple_functions.functions1 import factorial
__all__ = ['sin_series_sum']


@lru_cache(maxsize=None)
def sin_series_sum(x, n):
    """Uses Taylor's expansion to compute sin(x)
    """
    term = (-1)**n / factorial(2*n + 1) * x**(2*n+1)
    return term + sin_series_sum(x, n-1) if n else term
