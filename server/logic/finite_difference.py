import numpy as np
import scipy.linalg as sla

float_type = np.float64

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

def nth_derivative(f, x, n):
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

    h = np.float_power(10, -3)
    h_to_n = np.float_power(h, n)
    return [sum([np.divide(np.multiply(v[i], f(xi + np.multiply(samples[i], h))), h_to_n) for i in range(len(samples))]) for xi in x]


if __name__ == "__main__":
    # debug code
    # print(newton(lambda x: (x**4), 2, 3))
    # print(lanczo(lambda x: (x**4), 2, 3))
    print(nth_derivative(lambda x: (x**4), 2, 3))



