from . import TrueValue, newton_implementation
import numpy as np
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application


def true(expr, value, n):
    return TrueValue.nth_derivative(expr, symbols('x'), n, value)


def newton(expr, value, n):
    def f(x): return expr.subs(symbols('x'), x)
    return newton_implementation.nth_derivative(f, value, n)


def getAllDerivatives(formula, v, n):
    trueValue = true(formula, v, n)
    newtonValue = newton(formula, v, n)
    return {
        'x': v,
        'true': {
            'val': float(trueValue)
        },
        'newton': {
            'val': float(newtonValue),
            'relErr': float(abs((newtonValue - trueValue)/trueValue))
        }
    }


def getAllDerivativesForInterval(expr: str, start: str, end: str, n: str, points: str):
    transformations = (standard_transformations +
                       (implicit_multiplication_application,))
    formula = parse_expr(expr, transformations=transformations)
    n = int(n)
    start = float(start)
    end = float(end)
    points = int(points)

    interval = np.linspace(start, end, points)
    res = [getAllDerivatives(formula, i, n) for i in interval]
    return res
