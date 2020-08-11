import numpy as np
from scipy.special import legendre
from scipy.integrate import quad
def integral(u, f, x, h, n):
    leg = legendre(n)
    l = leg(u)
    return f(x+h*u)*l
def Lanczo(f,x,n):
    leg = legendre(n)
    h = np.float_power(10,-3)
    ans = np.math.factorial(2*n+1)/(2**(n+1)*np.math.factorial(n)*h**n)
    q = quad(integral,-1.0,1.0, args = (f,x,h,n))
    ans*=q[0]
    return ans

if __name__=="__main__":
    print(Lanczo(lambda x: (np.sin(x)), np.pi, 4))
