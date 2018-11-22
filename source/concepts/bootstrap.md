Bootstrap
---------

Bootstrapping is a method to construct empiric distributions of various 
statistics (mean, confidence intervals, deviation, etc) by using repreated 
sampling from an observed dataset.

A little magic is [why exactly][stats-why-bp-works] taking random samples 
like `[1,1,2]`, `[3,2,2]`, `[2,1,3]`, etc is a good idea to approximate 
properties of a dataset `[1,2,3]`. 

[stats-why-bp-works]: https://stats.stackexchange.com/questions/26088/explaining-to-laypeople-why-bootstrapping-works

Bootstrap originally proposed by [Bradley Efron in 1979](http://jeti.uni-freiburg.de/studenten_seminar/stud_sem_SS_09/EfronBootstrap.pdf).
For formal introduction see [Horowitz chapter in Handbook of Econometrics](https://www.sciencedirect.com/science/article/pii/S157344120105005X) (2001) and a usage  overview by [MacKinnon 2006](https://core.ac.uk/download/pdf/6494253.pdf).

[![](https://www.statisticshowto.datasciencecentral.com/wp-content/uploads/2016/10/bootstrap-sample.png)](https://www.statisticshowto.datasciencecentral.com/bootstrap-sample/)


### Toy example

[Bootstrap confidence intervals by Jeremy Orloff and Jonathan Bloom, pp. 4-6](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading24.pdf) provides the following basic code example
for bootstrap. Their full code for this excercise is [here](https://math.mit.edu/~dav/05.dir/class24-empiricalbootstrap.r).


```R
# Example. Empirical bootstrap confidence interval for the mean.
# Data for the example in class24-prep
cat("Example. Empirical boostrap confidence interval for the mean.",'\n')
x = c(30,37,36,43,42,43,43,46,41,42)
n = length(x)
set.seed(1)  # for repeatability

# sample mean
xbar = mean(x)
cat("data mean = ",xbar,'\n')
nboot = 20
# Generate 20 bootstrap samples, i.e. an n x 20 array of
# random resamples from x.
tmpdata = sample(x,n*nboot, replace=TRUE)
bootstrapsample = matrix(tmpdata, nrow=n, ncol=nboot)

# Compute the means xbar*
xbarstar = colMeans(bootstrapsample)

# Compute delta* for each bootstrap sample
deltastar = xbarstar - xbar

# Find the 0.1 and 0.9 quantiles for deltastar
d = quantile(deltastar,c(0.1,0.9))

# Calculate the 80\% confidence interval for the mean.
ci = xbar - c(d[2],d[1])
cat('Bootstrap confidence interval: [',ci,']','\n')
```

#### Bootstrap do’s and don’ts by Anna Mikusheva 

> - If you have a pivotal statistic,  bootstrap can give a refinement.  So, if you have choice 
>   of statistics, bootstrap a pivotal one.
> - Bootstrap may fix a finite-sample bias, but cannot help if you have inconsistent estimator.
> - In  general,  if  something  does  not  work  with  traditional  asymptotics,  the  
>   bootstrap  cannot  fix  your problem. For example, if we have an inconsistent estimate, the 
>   bootstrap bias correction does not fix anything.
> - Bootstrap could not fix the following problems: weak instruments, parameter on a boundary, 
>   unit root, persistent regressors.
> - Bootstrap requires re-centering (the null hypothesis to be true).

Source: [MIT lecture notes](https://ocw.mit.edu/courses/economics/14-384-time-series-analysis-fall-2013/lecture-notes/MIT14_384F13_lec9.pdf)

### More links (preliminary)

- https://core.ac.uk/download/pdf/6494253.pdf
- https://github.com/wmutschl/GMMIndirectInferenceBootstrap
- https://www.schmidheiny.name/teaching/bootstrap2up.pdf
- http://rosetta.ahmedmoustafa.io/bootstrap/
- http://www.cs.cornell.edu/courses/cs1380/2018sp/textbook/chapters/11/2/bootstrap.html


### Editor notes

- [Russian article][bp_ru] in Wikipedia on bootstrap is much more concise and understandable 
than [English one][bp_ru].

[bp_ru]: https://ru.wikipedia.org/wiki/%D0%91%D1%83%D1%82%D1%81%D1%82%D1%80%D1%8D%D0%BF_(%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0)

[bp_en]: https://en.wikipedia.org/wiki/Bootstrapping_(statistics)
