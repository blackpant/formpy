import math

def solver(a, b, c):
    """
    >>> solver(1, 6, 2)
    Traceback (most recent call last):
    ...
    ValueError: Discriminant negatif
    >>> solver(2, 1, 0)
    (0, -0.5)
    >>> solver(7, 6, 2)
    Traceback (most recent call last):
    ...
    ValueError: Discriminant negatif
    """
    d= b ** 2 - 4 * a * c
    if d >= 0:
        disc = math.sqrt(d)
        r1 = (-b + disc) / (2 * a)
        r2 = (-b - disc) / (2 * a)
        return r1, r2
    else:
        raise ValueError('Discriminant negatif')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
