Maximum likelihood
==================

The density function `f(x, θ)` tells you a probability of occurrence 
of a value in the proximity of `x`.  `f(x, θ)` has one or several parameters `θ`. 
We often want to know the estimate of the unknown parameter `θ` given 
the observed sample `(x1, x2, ... xn)`. 

Let's consider the following event definition: the sample `(x1, x2, ... xn)` is 
a draw of `n` independent random variables taken from `f(x, θ)` distribution. 
This event has a probability (likelihood) `L(θ)` which is equal to a product of 
individual probabilities: `L(θ) = f(x1, θ)*f(x2, θ)*...*f(xn, θ)`. We call  `L(θ)` a 
likelihood function `L(θ)` and would like to  find a `θ` that maximises it.  By 
maximising  `L(θ)` on `θ` we are searching for a parameter `θ1` under which it is most 
likely that `(x1, x2, ... xn)` are really coming from `f(x, θ1)`. 


Pedagogic difficulties 
----------------------

Links
-----

- Nice example with [weight of mice](https://nsu.ru/mmf/tvims/chernova/ms/lec/node14.html)

- Best of [Stack Overflow issues](https://stats.stackexchange.com/questions/112451/maximum-likelihood-estimation-mle-in-layman-terms)

- [Very accessible treatment of ML (in Russian)](https://nsu.ru/mmf/tvims/chernova/ms/lec/node14.html)


Notes
-----

1. **Joint probability.** The probability of occurence of individual `x1` is `f(x1, θ)`.  As the joint probability of independent events in a product of individual probabilties, the probability of occurence two draws is `f(x1, θ)*f(x2, θ)` and for all `n` draws it is `f(x1, θ)*f(x2, θ)*...*f(xn, θ)`. 


