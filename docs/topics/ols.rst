Ordinary least squares, OLS
---------------------------

OLS is at the core of econometrics curriculum, it is easily derived and
highly practical to familiarise a learner with regression possibilites
and limitations.

The usual way to teach OLS is to present assumptions and show how to deal
with their violations as indicated below in a review chart from Kennedy's
textbook.


.. image:: _static/peter_kennedy_on_ols.png


Math:

:math:`Y = \beta X + \epsilon`, :math:`\epsilon` is iid, normal with finite variance.

Common steps: 

1. specify model: select explanatory variables, transform them if needed 
2. estimate coefficients 
3. elaborate on model quality (the hardest part) 
4. go to 1 if needed 
5. know what model *does not* show (next hardeer part)

What may go wrong: 

- residuals are not random 
- variables are cointegrated 
- multicollinearity in regressors 
- residuals depend on x (heteroscedasticity) 
- inference is not causality 
- wrong signs, insignificant coefficients 
- variable normalisation was not described

Discussion: 

- why sum of squares as a loss function? 
- connections to bayesian estimation
- is R2 useful or dangerous?

Implementations:

-  `lm function in
   R <https://github.com/wch/r-source/blob/0f07757ad10ca31251b28a2c332812e63c0acf38/src/library/stats/R/lm.R>`__
-  `OLS class in python
   statsmodels <https://github.com/statsmodels/statsmodels/blob/master/statsmodels/regression/linear_model.py>`__
-  `python scypi least
   squares <https://github.com/scipy/scipy/blob/v1.1.0/scipy/linalg/basic.py#L1048-L1265>`__
-  julia `Alistair <https://github.com/giob1994/Alistair.jl>`__, GLM.jl,
   Regression.jl
-  `Replication
   examples <https://www.kaggle.com/nicapotato/in-depth-simple-linear-regression>`__
-  check unsorted `links about OLS <ols_links.txt>`__ - but it is not
   better than googling on your own

Baby dragon special:

.. raw:: html

   <embed>
   <blockquote class="twitter-tweet"><p lang="en" dir="ltr">The cutest thread you’ll ever read about multiple linear regression 😄👇🏼👇🏼 <a href="https://t.co/3lyil1IQV5">https://t.co/3lyil1IQV5</a></p>&mdash; Ellie Murray: sleeping, dont wake til Monday (@EpiEllie) <a href="https://twitter.com/EpiEllie/status/1197762932441931777?ref_src=twsrc%5Etfw">November 22, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
   </embed>