Analysis of variance (ANOVA)
============================

- ANOVA can mean several things: actual decomposition of variance, comparing the group means or representation of regression results
- Boils down to a regression with dummy (categorical) variables
- Heavy traction in terminolgy from design of exepriments (see definitons section [here](https://en.wikipedia.org/wiki/Analysis_of_variance))
- Standartised result tables with `SS`, `DF`, `MSS`, `F`, `p`
- Frightening multitude of R packages
- May want to look at a simple reference case [here](https://www.itl.nist.gov/div898/strd/anova/SiRstv.html)


Quote:

> *ANOVA can be seen as "syntactic sugar" for a special subgroup of linear regression models. ANOVA is regularly used by researchers who are not statisticians by training. They are now "institutionalized" and its hard to convert them back to using the more general representation* [suncoolsu](https://stats.stackexchange.com/users/1307/suncoolsu)


Code examples
-------------

- <https://stackoverflow.com/questions/25537399/anova-in-python-using-pandas-dataframe-with-statsmodels-or-scipy>

- <http://www.statsmodels.org/devel/anova.html>

- https://stats.stackexchange.com/a/175265/211794
  
- also possibly in Think Stats and [Hadley Wickham](https://stats.stackexchange.com/a/5283/211794)
 

Links
-----

Intro by [Jim](http://statisticsbyjim.com/anova/)

Cross-Validated has several general discussions:

- [why-is-anova-taught-used-as-if-it-is-a-different-research-methodology-compared](https://stats.stackexchange.com/questions/555/why-is-anova-taught-used-as-if-it-is-a-different-research-methodology-compared)
- [how-to-visualize-what-anova-does](https://stats.stackexchange.com/questions/5278/how-to-visualize-what-anova-does)
- [how-to-interpret-f-and-p-value-in-anova](https://stats.stackexchange.com/questions/12398/how-to-interpret-f-and-p-value-in-anova)
- [good-resource-to-understand-anova-and-ancova](https://stats.stackexchange.com/questions/2730/good-resource-to-understand-anova-and-ancova)

... followed by ANOVA vs regression:

- [difference-between-regression-analysis-and-analysis-of-variance](https://stats.stackexchange.com/questions/34616/difference-between-regression-analysis-and-analysis-of-variance)
- [why-is-anova-equivalent-to-linear-regression](https://stats.stackexchange.com/questions/175246/why-is-anova-equivalent-to-linear-regression)


NIST Handbook deals with ANOVA assumptions and interepations, as well as provides reference datasets: 

   - [The one-way ANOVA model and assumptions](https://www.itl.nist.gov/div898/handbook/prc/section4/prc432.htm)
   - [Interpretation of the ANOVA table](https://www.itl.nist.gov/div898/handbook/prc/section4/prc433.htm)
   - [Reference datasets and regresion results](https://www.itl.nist.gov/div898/strd/anova/anova.html)

Very simple and illustrative case NIST reference case [here](https://www.itl.nist.gov/div898/strd/anova/SiRstv.html).


Comoact Julia package [ANOVA.jl](https://github.com/marcpabst/ANOVA.jl) at about 150 lines of code, but not as much documentation yet.


ANOVA is again a case where [Russian wikipedia][ru] is more concise and clear on the subject.

[ru]: https://ru.wikipedia.org/wiki/%D0%94%D0%B8%D1%81%D0%BF%D0%B5%D1%80%D1%81%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7

'Types' of sum of squares and associated confusion:
- https://mcfromnz.wordpress.com/2011/03/02/anova-type-iiiiii-ss-explained/
- https://rcompanion.org/rcompanion/d_04.html
- https://stats.stackexchange.com/questions/20452/how-to-interpret-type-i-type-ii-and-type-iii-anova-and-manova

References
----------

Gelman, A. (2005). Analysis of variance: why it is more important than ever (with discussion). Annals of Statistics 33, 1–53. doi:10.1214/009053604000001048