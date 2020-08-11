import numpy as np

float_type = np.float32


def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def lanczo(f, x, n):
    s = 0
    h = np.float_power(10, -3)
    for k in range(n+1):
        s += (-1)**(k+n)*choose(n, k)*f(x+k*h)
    return s/(h**n)


def newton(f, x, n):
    x = float_type(x)
    h = np.multiply(np.sqrt(np.finfo(float_type).eps), x)
    if x == 0:
        h = float_type(np.power(10, -5))
    _sum = float_type(0)
    for k in range(n+1):
        if (k + n) % 2 == 0:
            _const = float_type(choose(n, k))
        else:
            _const = float_type(-1 * choose(n, k))
        summand = np.multiply(
            _const, f(np.add(float_type(x), np.multiply(float_type(k), h))))
        _sum = np.add(_sum, summand)
    h_to_n = np.power(h, n)
    print(h)
    return np.multiply(np.divide(float_type(1), h_to_n), _sum)


if __name__ == "__main__":
    # debug code
    print(newton(lambda x: (x**4), 2, 3))
    print(lanczo(lambda x: (x**4), 2, 3))
