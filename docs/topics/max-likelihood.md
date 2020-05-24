Maximum likelihood
==================

The probability density function `p = f(x, θ)` tells you a probability of occurrence 
of a random value near `x`.  Likelihood is a reverse operation of estimating unknown paramter `θ` from the same equation using `p` and `x`.

## Lead by example: pick the proper Gaussian

- Observations
- Probability of observations
- Observed sample is considered the most likely one
- Maximisation of probability allows to compute distribution parameters 

### 1. Observations.

Consider an experiment where we draw two random indepenent values `(x₁, x₂)` from the same distribution, e.g. the weight of two [mice][mice] in grams `(30, 50)`. There is some prior knowledge given to you that the distribution is normal with a center around `μ` (average mouse weight) and standard deviation of `σ`: `x ~ N(μ, σ²)`. 

### 2. Probability of observations. 

What was the probability of encountering `(x₁, x₂) = (30, 50)`? It is the product of individual event probabilities `L = f(x₁) · f(x₂)`. This value itself depends on  unknown `μ` and `σ`, so can be written as `L(μ, σ) = f(x₁ | μ, σ) · f(x₂ | μ, σ)`,  where `f` is probability density function.   

### 3. Observed sample is considered the most likely one.

It is prudent to assume that observed `(x₁, x₂) = (30, 50)` was the realisation of the most probable possible event. This way we take good use of available scarce information and make a better guess. If we decide we just saw an extreme event, we will be systematically wrong on this decision ([a tourist sees a working fountain in town][fountain] provides extra intuition).


### 4. Maximisation of probability allows to compute distribution parameters.

So, upon a fact of observation of `(x₁, x₂)` we tend to believe this has to be an event with 
maximum probability (likelihood) of happening. From this assumption we can find `μ` and `σ`
that maximise `L`. Sometimes it is possible to do it analytically, as with normal 
distributions, sometimes we have to search for solution numerically (hoping it is unique).

## Generalisation of example above

We usualy denote a set of parameters like `μ` and `σ` as `θ`, a vector of parameters.
Our task is to estimate parameter `θ` given:

- a sample of observations of а random variable `X = (x₁, x₂, ..., xₙ)`, and
- a pre-defined probability density function `f(x, θ)`. 
 
**Solution steps:**

1. Collect observations `X = (x₁, x₂, ..., xₙ)`
2. Make a decision about which probability density function `f(x, θ)` is appropriate
   for this data
3. Compose joint probability of observations as a function of `θ`: 
   `L(θ) = f(x₁, θ)·f(x₂, θ)· ...·f(xₙ, θ)`.
4. Come to terms with a principle "if we really did observe this event, it was 
   the most probable outcome of all possible events given this distribution" 
5. Find which `θ` maiximises joint probability of observations


Code
----

Python code below below relies on `scipy.optimixe.minimize` solver 
to find parameters of a normal distribution based on two measurements 
of mice weights rom example above. It can be easily applied to more observations. 

```python
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
```

## Other code examples

- [Annotated R code by Andrew Collier (2013)][ab]
- [Doing Maximum Likelihood Estimation by Hand in R by John Myles White (2010)][jw] 
- [Review of the Mathematics of Logistic Regression via MLE (2020)][jw2] 
   and [follow-up comments here](https://twitter.com/johnmyleswhite/status/1264355256974168067)
- [Julia vs R vs Python Simple Optimization by Zhuo Jiadai (2018)][zh]

[ab]: https://datawookie.netlify.com/blog/2013/08/fitting-a-model-by-maximum-likelihood
[jw]: http://www.johnmyleswhite.com/notebook/2010/04/21/doing-maximum-likelihood-estimation-by-hand-in-r
[jw2]: https://github.com/johnmyleswhite/julia_tutorials/blob/master/Statistics%20in%20Julia%20-%20Maximum%20Likelihood%20Estimation.ipynb
[zh]: https://www.codementor.io/zhuojiadai/julia-vs-r-vs-python-simple-optimization-gnqi4njro

## Links


- Nice video with [weight of mice][mice]

[mice]: https://www.youtube.com/watch?v=XepXtl9YKwc

- [Maximum likelihood estimation in layman terms](https://stats.stackexchange.com/questions/112451/maximum-likelihood-estimation-mle-in-layman-terms)

> Say you have some data. Say you're willing to assume that the data comes from some distribution -- perhaps Gaussian. There are an infinite number of different Gaussians that the data could have come from (which correspond to the combination of the infinite number of means and variances that a Gaussian distribution can have). MLE will pick the Gaussian (i.e., the mean and variance) that is "most consistent" with your data (the precise meaning of consistent is explained below).

- [Why is maximum likelihood estimation considered to be a frequentist technique](https://stats.stackexchange.com/questions/180420/why-is-maximum-likelihood-estimation-considered-to-be-a-frequentist-technique/190695#190695)

## In Russian

- [Very accessible math treatment (in Russian)](https://nsu.ru/mmf/tvims/chernova/ms/lec/node14.html)

- [Tourist sees a fountain (also in Russian)][fountain]

[fountain]: https://www.youtube.com/watch?v=2iRIqkm1mug
