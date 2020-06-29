from sympy import diff, symbols, Float
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

def nth_derivative_from_string(expr: String, var: String, n: String, value: String):
    transformations = (standard_transformations + (implicit_multiplication_application,))
    formula = parse_expr(expr, transformations = transformations)
    return nth_derivative(formula, symbols(var), int(n), Float(value))

def nth_derivative(formula, var, n, value):
    derivative = diff(formula, var, n)
    return derivative.subs(var,value)
