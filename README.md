# Econometrics navigator

<https://epogrebnyak.github.io/econometrics-navigator>

## What is it?

*Econometrics navigator* is a open source guide to econometrics.
It is now at skeleton + examples stage.   

It looks like the sceleton will be:

1. an overview of econometric [concepts and techniques](source/themes/index.rst), featuring minimum working toy code to illustrate a topic   
2. selected Stack Overflow answers and [twitter posts](source/twitter.md) are first-class citizens
3. the ocean of on-line references is pearls amongst trash,
   and needs [a distillation of must-reads](source/references.md).
4. milestones articles in macro, finance, risk, policy evaluation and microeconomics is something I would have read myself ([draft](source/applications.md))
5. [data sources](source/data.md) and replicable research in econometrics (how many econometric articles do have code published on github?)

## Where is it?

The Navigator is located at <https://epogrebnyak.github.io/econometrics-navigator>.

## Tech stack

I write in markdown and put documentation together into HTML using [sphinx](http://www.sphinx-doc.org/en/master/). 
The HTML output is pushed to Github Pages. I'm hopeful to produce a nicely looking PDF using [pandoc](https://pandoc.org/) 
and LaTeX.
