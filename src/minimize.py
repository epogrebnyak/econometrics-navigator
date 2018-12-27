"""Minimise a function of two arguments.
"""
from numpy import isclose
from scipy.optimize import minimize

def f(x):
    # unpack x
    x1 = x[0]
    x2 = x[1]    
    return (x1-3)**2 + (x2+1)**2

# minimise f given initial guess x0 
p = minimize(f, x0=[0, 0])

# test result
assert p.success is True
p.x
# array([ 3.00000004, -1.00000007])
assert isclose(p.x[0], 3)
assert isclose(p.x[1], -1)