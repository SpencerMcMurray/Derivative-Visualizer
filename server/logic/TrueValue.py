from sympy import diff, symbols, Float

def nth_derivative(formula, var, n, value):
    derivative = diff(formula, var, n)
    return derivative.subs(var, value)
