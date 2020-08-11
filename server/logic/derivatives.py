import numpy as np
from scipy.special import legendre
from scipy.integrate import quad
import scipy.linalg as sla


float_type = np.float64


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

def sampling(n):
    #2n+1 samples
    return np.array([i for i in range(-n, n+1)])

def factorial(n):
    facts = [1]
    for i in range(1, n + 1):
        facts.append(facts[-1]*i)
    return facts[-1]

def find_middle(xs):
    if np.size(xs) % 2 == 0:
        return xs[int(np.size(xs)/2)]
    else:
        return xs[int((np.size(xs) - 1)/2)]

def finite_difference(f, x, n):
    samples = sampling(n)
    mat = np.array([
        [np.power(samples[i], j) for i in range(len(samples))] for j in range(len(samples))
    ])
    
    b = np.zeros(len(samples)).transpose()
    b[n] += factorial(n)

    L, U = sla.lu(mat, permute_l=True)
    y = sla.solve(L, b)
    v = sla.solve(U, y)
    if isinstance(x, int):
        x = np.array([x])
    mid = find_middle(x)
 

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
    print(finite_difference(lambda x: (x**4), 2, 3))

