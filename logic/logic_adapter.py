from . import TrueValue, newton_implementation
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def true(expr: str, value: str, n:str):
    transformations = (standard_transformations +
                       (implicit_multiplication_application,))
    formula = parse_expr(expr, transformations=transformations)
    return TrueValue.nth_derivative(formula, symbols('x'), int(n), float(value))

def newton(expr: str, value: str, n: str):
    transformations = (standard_transformations + (implicit_multiplication_application,))
    formula = parse_expr(expr, transformations = transformations)
    f = lambda x: formula.subs(symbols('x'), x)
    return newton_implementation.nth_derivative(f, float(value), int(n))
    