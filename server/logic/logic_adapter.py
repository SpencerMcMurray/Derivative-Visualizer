from . import TrueValue, newton_implementation, Lanczo
import numpy as np
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application


def true(expr, value, n):
    return TrueValue.nth_derivative(expr, symbols('x'), n, value)


def newton(expr, value, n):
    def f(x): return expr.subs(symbols('x'), x)
    return newton_implementation.nth_derivative(f, value, n)

def lanczo(expr, value, n):
    def f(x): return expr.subs(symbols('x'), x)
    ys = [Lanczo.Lanczo(f, x, n) for x in value]
    return ys

def getAllDerivatives(formula, v, n):
    trueValue = true(formula, v, n)
    newtonValue = newton(formula, v, n)
    t = float(trueValue)
    nt, nt_err = float(newtonValue), float(
        abs((newtonValue - trueValue)/trueValue))
    return t, nt, nt_err


def getAllDerivativesForInterval(expr: str, start: str, end: str, n: str, points: str):
    transformations = (standard_transformations +
                       (implicit_multiplication_application,))
    formula = parse_expr(expr, transformations=transformations)
    n = int(n)
    start = float(start)
    end = float(end)
    points = int(points)

    interval = np.linspace(start, end, points)
    t_list, nt_list, nt_err_list = [], [], []
    for x in interval:
        t, nt, nt_err = getAllDerivatives(formula, x, n)
        t_list.append(t)
        nt_list.append(nt)
        nt_err_list.append(nt_err)
    return t_list, nt_list, nt_err_list, interval
