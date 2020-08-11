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


def nth_derivative(f, x, n):
    x = float_type(x)
    h = np.multiply(np.sqrt(np.finfo(float_type).eps), x)
    if x == 0:
        h = float_type(np.power(10, -5))
    _sum = float_type(0)
    for k in range(n+1):
        s += (-1)**(k+n)*choose(n, k)*f(x+k*h)
    return s/(h**n)


if __name__ == "__main__":
    # debug code
    print(nth_derivative(lambda x: (x**4), 2, 3))
