from . import TrueValue, derivatives
import numpy as np
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

NUM_METHODS = 2


def true(expr, value, n):
    return TrueValue.nth_derivative(expr, symbols('x'), n, value)


def get_rel_err(v, t):
    return float(v), float(abs((v - t)/t))

def lanczo(expr, value, n):
    def f(x): return expr.subs(symbols('x'), x)
    ys = [Lanczo.Lanczo(f, x, n) for x in value]
    return ys

def getAllDerivatives(formula, v, n):
    trueValue = true(formula, v, n)
    def f(x): return formula.subs(symbols('x'), x)

    newtonValue = derivatives.newton(f, v, n)
    lanczoValue = derivatives.lanczo(f, v, n)
    t = float(trueValue)
    vals = [get_rel_err(newtonValue, trueValue),
            get_rel_err(lanczoValue, trueValue)]
    return t, vals


def getAllDerivativesForInterval(expr: str, start: str, end: str, n: str, points: str):
    transformations = (standard_transformations +
                       (implicit_multiplication_application,))
    formula = parse_expr(expr, transformations=transformations)
    n = int(n)
    start = float(start)
    end = float(end)
    points = int(points)

    interval = np.linspace(start, end, points)
    t_list, dt_list, dt_err_list = [], [], []
    for i in range(NUM_METHODS):
        dt_list.append([])
        dt_err_list.append([])
    for x in interval:
        t, vals = getAllDerivatives(formula, x, n)
        t_list.append(t)
        for i, d in enumerate(vals):
            dt_list[i].append(d[0])
            dt_err_list[i].append(d[1])
    return t_list, dt_list, dt_err_list, interval
