Contents in brief  
=================

```
Introduction 
1. Interviews
2. Methods and concepts reference
3. Usecases - replication work
Appendices
```

Notes
=====

- Available tutorials are endless, but some meaningless 
- Cannot really substitute a course or a book with internet browsing
- Maybe develop own format on how to talk briefly about topics - 
  eg extended dictionary?
- There is code availble to inspect in statmodels, R and julia, 
  can browse into it. 
- Our way: experiment with code, systematize readings, nurture intuition.
- Todo: compile to pdf and print hard copy

Contents
========

Introduction

1. Interview with EL + other short interviews

2. Reference of concepts and methods
  - Estimation 
     - OLS
     - Max Likelihood
     - Bayesian estimation
  - Time series
  - Panel data
  - Classification

3. Usecases - replication of articles 
   (macro, finance, risk and microeconomics)

Appendix:
    - Appendix 1: Econometrix mindmap
    - Appendix 2: Annotated bibliography
    - Appendix 3: History of econometrics

Mind map
========

Microeconometrics
Macroeconometrics
Outside economics

OLS -> GMM
Max Likelihood 
Bayesian estimation 

Time series
Panel
Cross section  

Dictionary
==========

1. Ordinary least squares, OLS
-------------------------------

Math: Y = BX + e    

Assumptions:
   e is normally distributed

Common steps:
   0. think of what may explain what
   1. specify model: select regressors, transform variables
   2. estimate coefficients
   3. elaborate on model quality (hardest part) 
   4. to go 0 or 1 if needed
   5. know what model *does not* show (next hardest part)

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
   
Replication examples:
   - <https://www.kaggle.com/nicapotato/in-depth-simple-linear-regression>   

Links:

2. Principal components analysis, PCA
-------------------------------------

Math:
Assumptions:
Usual steps:
What may go wrong:
Discussion:
Replication examples:
   - ...

Links:
 - https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues/2700#2700
 - https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_3d.html#sphx-glr-auto-examples-decomposition-plot-pca-3d-py
 - https://stats.stackexchange.com/questions/48214/replicating-shalizis-new-york-times-pca-example?rq=1

More topics
-----------

OLS Extensions:
- GMM, 2,3 stage OLS
- quantile regressions 
- lasso, rigde

Estimation:
- maximum likelihood
- bayesian estimation
- mcmc (see reddit post)

Time series:
- time series, stationarity, unit root
- state space representation, Kalman filter
- fractional integration
- seasonal adjustment
- (vector) error correction model, VECM
- structural breaks 

Other:

- [bootstrap](https://www.schmidheiny.name/teaching/bootstrap2up.pdf)


Concepts
--------
- bias-variance tradeoff
- indentification
- [Bayes theorem](http://onlinestatbook.com/2/probability/bayes_demo.html)
- inference 
- overfitting
- replication, replicability
- Lucas critique
- [causality (not 'casuality')](https://chrisaulddotcom.wordpress.com/2013/10/08/remarks-on-chen-and-pearl-on-causality-in-econometrics-textbooks/)
- [spurious regression](https://mpra.ub.uni-muenchen.de/59008/)


Applications
------------

Macro: 
   - GDP
   - FX
   - interest rates
   - asset class allocation 
   - business cycle 

Risks and finance:
   - VAR    
   - search of invariants (Atillo Meucci)

Panel data:
   - *MHE*
   - policy assessment

History of econometrics
-----------------------

   <history.md>
   