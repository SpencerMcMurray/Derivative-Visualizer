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


def nth_derivative (f, x, n):
    x = float_type(x)
    #h = np.multiply(np.sqrt(np.finfo(float_type).eps), x)
    h = float_type(np.float_power(10,-5))
    _sum = float_type(0)
    for k in range(n+1):
        if (k + n) % 2 == 0:
            _const = float_type(choose(n, k))
        else: 
            _const = float_type(-1 * choose(n, k))
        summand = np.multiply(_const, f(np.add(float_type(x), np.multiply(float_type(k), h))))
        _sum = np.add(_sum, summand)
    h_to_n = np.power(h, n)
    print(h)
    return np.multiply(np.divide(float_type(1), h_to_n), _sum)

def new_nth_derivative(f,x,n):
    h = 0.0001
    s = 0
    for k in range(n+1):
        s += ((-1)**(k+n))*choose(n,k)*f(x+k*h)
    return s/np.power(h,n)

if __name__ == "__main__":
    # debug code
    print(nth_derivative(lambda x: (np.cos(x)), np.pi/2, 1))
    print(new_nth_derivative(lambda x: (np.cos(x)), np.pi/2, 1))
