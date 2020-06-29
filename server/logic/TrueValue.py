from sympy import diff, symbols
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

def nth_derivative_from_string(stringExpr, stringVar, n, value):
    transformations = (standard_transformations + (implicit_multiplication_application,))
    formula = parse_expr(stringExpr, transformations = transformations)
    var = symbols(stringVar)
    return nth_derivative(formula, var, n, value)

def nth_derivative(formula, var, n, value):
    derivative = diff(formula, var, n)
    return derivative.subs(var,value)
