import numpy as np
from scipy.special import legendre
from scipy.integrate import quad


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

def integral(u, f, x, h, n):
    leg = legendre(n)
    l = leg(u)
    return f(x+h*u)*l

def lanczo(f, x, n):
    leg = legendre(n)
    h = np.float_power(10,-3)
    ans = np.math.factorial(2*n+1)/(2**(n+1)*np.math.factorial(n)*h**n)
    q = quad(integral,-1.0,1.0, args = (f,x,h,n))
    ans*=q[0]
    return ans


def newton(f, x, n):
    s = 0
    h = np.float_power(10, -3)
    for k in range(n+1):
        s += (-1)**(k+n)*choose(n, k)*f(x+k*h)
    return s/(h**n)


if __name__ == "__main__":
    # debug code
    print(newton(lambda x: (x**4), 2, 3))
    print(lanczo(lambda x: (x**4), 2, 3))
