from . import TrueValue, derivatives
import numpy as np
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

NUM_METHODS = 3
APPROX_ROUND = 7
ERROR_ROUND = 10
XS_ROUND = 3


def true(expr, value, n):
    return TrueValue.nth_derivative(expr, symbols('x'), n, value)


def get_rel_err(v, t):
    if t == 0:
        rel_err = float(abs(v-t))
    else:
        rel_err = float(abs(v-t)/abs(t))
    return float(v), rel_err


def lanczo(expr, value, n):
    def f(x): return expr.subs(symbols('x'), x)
    if not isinstance(value, np.array):
        value = np.array([value])
    ys = [derivatives.lanczo(f, x, n) for x in value]
    return ys


def getAllDerivatives(formula, v, n):
    trueValue = true(formula, v, n)
    def f(x): return formula.subs(symbols('x'), x)

    newtonValue = derivatives.newton(f, v, n)
    lanczoValue = derivatives.lanczo(f, v, n)
    finiteValue = derivatives.finite_difference(f, v, n)
    t = float(trueValue)
    vals = [get_rel_err(newtonValue, trueValue),
            get_rel_err(lanczoValue, trueValue),
            get_rel_err(finiteValue, trueValue)]
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
            dt_list[i].append(round(d[0], APPROX_ROUND))
            dt_err_list[i].append(round(d[1], ERROR_ROUND))
    return t_list, dt_list, dt_err_list, np.around(interval, XS_ROUND)
