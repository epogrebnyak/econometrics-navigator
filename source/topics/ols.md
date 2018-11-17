## Ordinary least squares, OLS

Math: Y = BX + e    

Assumptions:
   - e is normally distributed

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

- https://towardsdatascience.com/simple-linear-regression-2421076a5892
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1736184
- https://cfss.uchicago.edu/persp012_regression_diagnostics.html
- https://stats.stackexchange.com/questions/218156/what-are-some-of-the-most-common-misconceptions-about-linear-regression
- https://pdfs.semanticscholar.org/a410/ec58bd5ff80a4e7978955ab11d096af6d138.pdf
- [COMMON MISTEAKS MISTAKES IN USING STATISTICS: Spotting and Avoiding Them](https://web.ma.utexas.edu/users/mks/statmistakes/StatisticsMistakes.html)
- http://www2.sas.com/proceedings/sugi22/STATS/PAPER267.PDF
- https://towardsdatascience.com/simple-linear-regression-2421076a5892
- http://jeromyanglim.blogspot.com/2013/12/using-r-to-replicate-common-spss.html
- https://stat.hevra.haifa.ac.il/~gweiss/courses/Forecasting/CarPricesAnalysis.pdf
- http://www.nrcresearchpress.com/doi/10.1139/f73-072#.W-SvWuK_Pcs
- https://www.nejm.org/doi/full/10.1056/NEJM198512263132604
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2992018/ - medicine, nice!
- http://replication.uni-goettingen.de/wiki/index.php/Ordinary_least_squares_(OLS) - list of replications
- https://stats.stackexchange.com/questions/211707/replicating-a-linear-regression-example-from-hastie-tibshirani-and-friedman (replication from Hastie)