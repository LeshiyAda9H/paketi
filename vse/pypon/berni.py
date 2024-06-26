from math import factorial

def factor(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def berni(n, k):
    def bernpoly(x):
        x = factor(n, k) * (x ** k) * ((1 - x) ** (n - k))
        return x

    return bernpoly
