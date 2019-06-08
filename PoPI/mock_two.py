def sqrProd(x, y):
    return (x * y) ** 2


def power(a, n):
    if n == 0:
        return 1
    else:
        return power(a, n - 1) * a


if __name__ == "__main__":
    assert sqrProd(2, 5) == 100
    assert power(2, 3) == 8
