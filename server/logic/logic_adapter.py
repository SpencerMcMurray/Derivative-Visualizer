from . import TrueValue, newton_implementation
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application


def true(expr, value, n):
    return TrueValue.nth_derivative(expr, symbols('x'), n, value)


def newton(expr, value, n):
    def f(x): return expr.subs(symbols('x'), x)
    return newton_implementation.nth_derivative(f, value, n)


def getAll(expr: str, value: str, n: str):
    transformations = (standard_transformations +
                       (implicit_multiplication_application,))
    formula = parse_expr(expr, transformations=transformations)
    v = float(value)
    n = int(n)
    trueValue = true(formula, v, n)
    newtonValue = newton(formula, v, n)
    return {
        'trueValue': {
            'val': float(trueValue)
        },
        'newton': {
            'val': float(newtonValue),
            'relErr': float(abs((newtonValue - trueValue)/trueValue))
        }
    }
