"""
Maximum likelihood with two mice.
"""

import numpy as np
from scipy.optimize import minimize

def dnorm(x, mu=0, sigma=1):
    """Normal distribution probability density fucntion."""
    const = 1 / (sigma * np.sqrt(2 * np.pi)) 
    power = - (x - mu)**2 / (2 * sigma**2)
    return  const * np.exp(power)

def log_likelihood(observed_x): 
    """Sum of logs of probability densities at *observed_x*.
    Return:
       function of mu and sigma 
    """
    def foo(mu, sigma):
        logs = [np.log(dnorm(x, mu, sigma)) for x in observed_x]
        return sum(logs)
    return foo

def maximise(f, start_mu, start_sigma):
    """Return mu and lambda, which maximise *f*."""
    f = lambda p: -1 * l_func(mu=p[0], sigma=p[1])
    res = minimize(f, x0=[start_mu, start_sigma])
    return res.x[0], res.x[1]
    
# two mice weigths are given, similar to https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6143748/
events = [30, 50]
# construct likelihood as a function of unknown mu and sigma
l_func = log_likelihood(events)
# run maximisation procedure
# attention: need a sensible pick for start variables, eg (0, 1) will fail
estimated_mu, estimated_sd = maximise(l_func, start_mu=30, start_sigma=3)
      
# test outcomes
#estimated_mu is 39.99999527669165
assert np.isclose(estimated_mu, 40)
#estimated_sd is 9.999976480910071
assert np.isclose(estimated_sd, 10)

# Result: observed values [30, 50] were most likely coming from 
#         normal distribution with parameters μ=40 and σ=10.